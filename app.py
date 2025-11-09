import os
from datetime import datetime, timezone

from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user
)
from flask_bcrypt import Bcrypt
from sqlalchemy import text

from models import Order, PumpkinDesign, User, db


app = Flask(__name__)
app.config.from_object('config')  # Load configuration from config.py

login_manager = LoginManager(app)
login_manager.login_view = "index"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorize_callback():
    return redirect(url_for("signup"))

bcrypt = Bcrypt(app)

with app.app_context():
    db.init_app(app)  # It connects the SQLAlchemy db object with the Flask app and the DBMS engine
    db.create_all()  # Create the database tables for all the models
     

@app.route('/')
def index():
    """ Render the homepage """
    return render_template('index.html')
    
@app.route('/signup', methods=["GET", "POST"])
def signup():
    """ Create the signup page and post a new user to the db """
    if request.method == "GET":
        return render_template('signup.html')
    elif request.method == "POST":
        password = request.form.get('password')
        hashed_password = bcrypt.generate_password_hash(password)
          
        user = User(
            username = request.form.get('username'),
            password = hashed_password,
            name=request.form["name"],
            email=request.form["email"],
            address=request.form["address"]
        )
        
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

        
@app.route('/login', methods=["GET", "POST"])
def login():
    """ Login page with password hashing """
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
    
        user = User.query.filter(User.username == username).first()    

        if bcrypt.check_password_hash(user.password, password):
            login_user(user)
            if current_user.role == 'admin':
               return redirect(url_for('admin_page')) # A special page for admins
            else:
                return redirect(url_for('index'))
        else:
            return 'Failed'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/create')
@login_required
def create_pumpkin_page():    
    return render_template('create.html')

@app.route("/create/submit", methods=["POST"])
@login_required
def create_pumpkin_action():
    """ Create new rows in the order and pumpkin_design tables """
    order = Order(
        # Generates a new order
        customer_id=current_user.user_id,
        status="Incomplete"
    )
    db.session.add(order)
    db.session.commit()
    # Aware that it's better to use get() so I can include defaults
    pumpkin = PumpkinDesign(
        size=request.form["size"],
        eyes=request.form["eyes"],
        mouth=request.form["mouth"],
        amount=request.form["amount"],
        order_id = order.order_id  # Adds the order id to the pumpkin_design table
    )
    
    db.session.add(pumpkin)
    db.session.commit()
    return redirect(url_for("order_submit", order_id=order.order_id))


@app.route("/create/add/<int:order_id>", methods=["GET"])
@login_required
def add_another_pumpkin(order_id):
    """ This page allows the user to add additional pumpkins to their order """
    order = Order.query.get_or_404(order_id)
    return render_template('add.html', order_id=order.order_id)

@app.route("/create/add/<int:order_id>", methods=["POST"])
@login_required
def add_another_action(order_id):
    order = Order.query.get_or_404(order_id)
    
    pumpkin = PumpkinDesign(
        size=request.form["size"],
        eyes=request.form["eyes"],
        mouth=request.form["mouth"],
        amount=request.form["amount"],
        order_id = order.order_id  # Adds the order_id to the pumpkin_design table
    )
    
    db.session.add(pumpkin)
    db.session.commit()
    
    return redirect(url_for("order_submit", order_id=order.order_id))

@app.route('/order/<int:order_id>', methods=["GET"])
@login_required
def order_submit(order_id):
    order = Order.query.get_or_404(order_id)
    if order.status == "Confirmed":
        return redirect(url_for("my_account")) # This is only relevant if the admin changes the order status before the user has completed their order
    return render_template('order.html', order=order)

@app.route("/order/<int:order_id>", methods=["POST"])
@login_required
def order_action(order_id):
    """ When the user confirms their order """
    order = Order.query.get_or_404(order_id)
    order.status = "Confirmed"
    db.session.commit()
    return redirect(url_for("order_thanks", order_id=order.order_id))


@app.route("/order/thank-you/<int:order_id>", methods=["GET"])
@login_required
def order_thanks(order_id):
    order = Order.query.get_or_404(order_id)
    return render_template('thanks.html', order=order)

@app.route("/order/<int:order_id>/delete", methods=["POST"])
@login_required
def delete_order(order_id):
    """ Used on the /order page to cancel an Incomplete order, 
    and on the /my-account page to cancel a Confirmed order """
    Order.query.filter(Order.order_id == order_id).delete()
    db.session.commit()
    return redirect(url_for("my_account"))

@app.route("/admin")
@login_required
def admin_page():
    orders = Order.query.order_by(Order.order_id).all()
    return render_template("admin.html", orders=orders)

@app.route("/my-account")
@login_required
def my_account():
    orders = Order.query.filter_by(customer_id=current_user.user_id).order_by(Order.order_id).all()
    # return (f"{current_user.user_id}")
    return render_template("my-account.html", orders=orders)

@app.route('/update_status/<int:order_id>', methods=['POST'])
@login_required
def update_status(order_id):
    new_status = request.form.get('status')
    order = Order.query.get_or_404(order_id)
    order.status = new_status
    db.session.commit()
    return redirect(request.referrer or url_for('orders'))



@app.route('/test')
def test_page():
    """ Ignore this for now. Just testing out queries. """
    result = db.session.execute(text('SELECT * FROM "order"'))
    rows = result.all()
    print (rows)
    return jsonify(rows)
    

        

# --- Seed defaults ---
def seed_defaults():
    if not User.query.first():  # Only seed if empty
        customer1 = User(username="bill", password=bcrypt.generate_password_hash("bill"), name="Bill S. Preston Esq.", email="bill@spreston.com", address="12 Avenue Lane, Cork", role="customer")
        customer2 = User(username="ted", password=bcrypt.generate_password_hash("ted"), name="Ted 'Theodore' Logan", email="ted@theodorelogan.com", address="43A Road Street, Limerick", role="customer")
        admin1 = User(username="admin", password=bcrypt.generate_password_hash("admin"), name="Pat Carver", email="pat@carv.com", address="32 Street Road, Galway", role="admin")
        
        db.session.add_all([customer1, customer2, admin1])
        db.session.commit()

    if not Order.query.first():  # Only seed if empty
        order1 = Order(order_id=1, created_at=datetime(2025, 10, 14, 15, 30), status="Delivered", customer_id=1)
        db.session.add_all([order1])
        db.session.commit()

    if not PumpkinDesign.query.first():  # Only seed if empty
        design1 = PumpkinDesign(design_id=1, size="large", eyes="scary", mouth="sad", amount=3, created_at=datetime(2025, 10, 14, 15, 30), order_id=1)
        db.session.add_all([design1])
        db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()   # Create tables if not exist
        seed_defaults()   # Add default data if empty
     
    # gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 app:app
  #  app.run(debug=True, port=8000)   Hiding this from Render

   