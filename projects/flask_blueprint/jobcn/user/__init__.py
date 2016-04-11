#coding=utf-8
from flask import Blueprint

# create a blueprint that named user
user = Blueprint(
    'user',
    __name__,
    template_folder='user_templates'
)

from . import views
