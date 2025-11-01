import os
from flask import Flask, render_template, request, redirect, url_for, session
from models import *


app = Flask(__name__)
app.config.from_object('config')  # Load configuration from config.py

@app.route('/')
def index():
    # Render the home page with all gigs
    return render_template('index.html')

@app.route('/create', methods=["GET"])
def create():
    # Render the 'Create' page
    return render_template('create.html')



if __name__ == '__main__':
     app.run(debug=True, port=8000)