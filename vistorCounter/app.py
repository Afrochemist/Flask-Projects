from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')




    db.init_app(app)
    migrate = Migrate(app,db)

    #import blueprints
    from counter.views import counter_app
    #register blueprints
    app.register_blueprint(counter_app)

    return app
