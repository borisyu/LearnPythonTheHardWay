from flask import render_template
from . import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/')
def user_home():
    return 'user home page'
