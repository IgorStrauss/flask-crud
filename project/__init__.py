from flask import Flask
from flask_migrate import Migrate

from project.models import db

Migrate()


def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
    app.config['SECRET_KEY'] = 'asdklj23476hkjda'

    db.init_app(app)
    Migrate(app, db)

    from project import urls
    urls.init_app(app)

    return app
