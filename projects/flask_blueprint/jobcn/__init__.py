#coding=utf-8
from flask import Flask
# from user package import user blueprint
from .user import user
from .company import company

# create a flask app
app = Flask(__name__)

# register user blueprint into app
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(company, url_prefix='/company')

from . import views
