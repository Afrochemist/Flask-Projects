from flask import Blueprint, render_template


main = Blueprint('main', __name__)

@main.route('/')
def index():
	return render_template('index.html')


@main.route('/sign')
def sign():
	return render_template('sign.html')