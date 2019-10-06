from flask import Flask


def create_app():
	app = Flask(__name__)

	from .views import main
	app.register_blueprint(main)

	return app




"""
cd ..
export FLASK_APP=commentStorage
flask run

"""