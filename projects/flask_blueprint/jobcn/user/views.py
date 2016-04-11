#coding=utf-8
from flask import render_template
# from local package import the user blueprint
from . import user

@user.route('/')
def index():
    return render_template('home.html')

@user.route('/resume')
def resume():
    return render_template('resume.html')
