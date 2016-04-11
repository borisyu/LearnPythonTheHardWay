from flask import render_template, request
from . import app

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    ip = request.headers.get('Remote-IP', None)
    return render_template('index.html', ua=user_agent, ip=ip)
