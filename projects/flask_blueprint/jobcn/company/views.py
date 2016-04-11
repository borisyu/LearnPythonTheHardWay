from flask import render_template
from . import company

@company.route('/')
def index():
    return render_template('home.html')
