import os
from flask import Flask, render_template, request, redirect, url_for, session
from models import *


app = Flask(__name__)
app.config.from_object('config')  # Load configuration from config.py


with app.app_context():
    db.init_app(app)  # It connects the SQLAlchemy db object with the Flask app and the DBMS engine
    db.create_all()  # Create the database tables for all the models
     

@app.route('/')
def index():
    # Render the home page
    return render_template('index.html')

@app.route('/create', methods=["GET"])
def create_pumpkin_page():
    # Render the 'Create' page
    
    return render_template('create.html')

@app.route("/create", methods=["POST"])
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
        order_id = order.order_id
    )
    
    db.session.add(pumpkin)
    db.session.commit()
    return redirect(url_for("order_submit", pumpkin_id=pumpkin.design_id))

@app.route('/order/<int:pumpkin_id>', methods=["GET"])
def order_submit(pumpkin_id):
    pumpkin = PumpkinDesign.query.get_or_404(pumpkin_id)
    return render_template('order.html', pumpkin=pumpkin)

@app.route("/order", methods=["POST"])
def order_action():
    # Action on submitting the form
    order = Order(
        
        # name=request.form["name"],
        # email=request.form["email"],
        # address=request.form["address"]
    )
    db.session.add(order)
    db.session.commit()
    return redirect(url_for("order_thanks", order_id=order.order_id))

@app.route('/order/thank-you/<int:order_id>', methods=["GET"])
def order_thanks(order_id):
    order = Order.query.get_or_404(order_id)
    return render_template('thanks.html', order=order)

# --- Seed defaults ---
def seed_defaults():
    if not Customer.query.first():  # Only seed if empty
        customer1 = Customer(name="Bill Preston", email="bill@preston.com", address="12 Avenue Lane, Cork")
        customer2 = Customer(name="Ted Logan", email="ted@logan.com", address="43A Road Street, Limerick")
        db.session.add_all([customer1, customer2])
        db.session.commit()
        print("✅ Default users added.")


    if not PumpkinDesign.query.first():  # Only seed if empty
        design1 = PumpkinDesign(design_id=1, size="Large", eyes="Scary", mouth="Sad", amount=3, created_at=datetime(2025, 10, 14, 15, 30))
        db.session.add_all([design1])
        db.session.commit()
        print("✅ Default designs added.")


   
    if not Order.query.first():  # Only seed if empty
        order1 = Order(order_id=1, created_at=datetime(2025, 10, 14, 15, 30), fulfilment="Carving")
        db.session.add_all([order1])
        db.session.commit()
        print("✅ Default designs added.")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()   # Create tables if not exist
        seed_defaults()   # Add default data if empty
     
    app.run(debug=True, port=8000)

   