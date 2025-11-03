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
    pumpkin = pumpkinDesign(
        size=request.form["size"],
        eyes=request.form["eyes"],
        mouth=request.form["mouth"],
        amount=request.form["amount"],
    )
    db.session.add(pumpkin)
    db.session.commit()
    return redirect(url_for("order_submit", pumpkin_id=pumpkin.designId))

@app.route('/order/<int:pumpkin_id>')
def order_submit(pumpkin_id):
    pumpkin = pumpkinDesign.query.get_or_404(pumpkin_id)
    return render_template('order.html', pumpkin=pumpkin)


if __name__ == '__main__':
     app.run(debug=True, port=8000)