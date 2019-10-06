from flask import Blueprint, render_template


main = Blueprint('main', __name__)

@main.route('/')
def index():
	return '<h1>Hello</h1>'

@main.route('/somethingelse')
def somethingelse():
	return '<h1>Something Else</h1>'