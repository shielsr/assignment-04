import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user,
)
from flask_bcrypt import Bcrypt

from models import *





app = Flask(__name__)
app.config.from_object('config')  # Load configuration from config.py

login_manager = LoginManager(app)
login_manager.login_view = "login_page"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

bcrypt = Bcrypt(app)

with app.app_context():
    db.init_app(app)  # It connects the SQLAlchemy db object with the Flask app and the DBMS engine
    db.create_all()  # Create the database tables for all the models
     

@app.route('/')
def index():
    # Render the home page
    return render_template('index.html')
    
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "GET":
        return render_template('signup.html')
    elif request.method == "POST":
        pass

@app.route('/login/<user_id>')
def login(user_id):
    user = User.query.get(user_id)
    login_user(user)
    return 'Success'

@app.route('/logout')
def logout():
    logout_user()
    return 'Logged out'

@app.route('/create')
def create_pumpkin_page():
    # Render the 'Create' page
    
    return render_template('create.html')

@app.route("/create/submit", methods=["POST"])
def create_pumpkin_action():
    # Action on submitting the form
    order = Order(
        # Generates a new order
    )
    db.session.add(order)
    db.session.commit()
    
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


@app.route("/create/add/<int:order_id>")
def add_another_pumpkin(order_id):
    order = Order.query.get_or_404(order_id)
    return render_template('add.html', order_id=order.order_id)

@app.route("/create/add/<int:order_id>", methods=["POST"])
def add_another_action(order_id):
    order = Order.query.get_or_404(order_id)
    
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

@app.route('/order/<int:order_id>', methods=["GET"])
def order_submit(order_id):
    order = Order.query.get_or_404(order_id)
    return render_template('order.html', order=order)

@app.route("/order/<int:order_id>", methods=["POST"])
def order_action(order_id):
    order = Order.query.get_or_404(order_id)
    order.status = "Order placed"
    db.session.commit()
    return redirect(url_for("order_thanks", order_id=order.order_id))


@app.route('/order/thank-you/<int:order_id>', methods=["GET"])
def order_thanks(order_id):
    order = Order.query.get_or_404(order_id)
    return render_template('thanks.html', order=order)


# @app.route("/admin")
# def admin_page():
#    return render_template("admin.html", orders=Order.query.all(), pumpkins=PumpkinDesign.query.all())

@app.route("/admin")
def admin_page():
    orders = Order.query.order_by(Order.order_id).all()
    return render_template("admin.html", orders=orders)


# --- Seed defaults ---
def seed_defaults():
    if not User.query.first():  # Only seed if empty
        customer1 = User(username="billpreston", password="1234asdf", name="Bill S. Preston", email="bill@spreston.com", address="12 Avenue Lane, Cork", role="customer")
        customer2 = User(username="tedlogan", password="asdf1234", name="Ted Theodore Logan", email="ted@theodorelogan.com", address="43A Road Street, Limerick", role="customer")
        db.session.add_all([customer1, customer2])
        db.session.commit()

    if not PumpkinDesign.query.first():  # Only seed if empty
        design1 = PumpkinDesign(design_id=1, size="Large", eyes="Scary", mouth="Sad", amount=3, created_at=datetime(2025, 10, 14, 15, 30), order_id=1)
        db.session.add_all([design1])
        db.session.commit()


   
    if not Order.query.first():  # Only seed if empty
        order1 = Order(order_id=1, created_at=datetime(2025, 10, 14, 15, 30), status="Order placed")
        db.session.add_all([order1])
        db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()   # Create tables if not exist
        seed_defaults()   # Add default data if empty
     
    app.run(debug=True, port=8000)

   