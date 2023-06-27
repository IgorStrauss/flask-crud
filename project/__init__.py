import os

from flask import Flask
from flask_migrate import Migrate

from project.models import db

Migrate()


def create_app():

    app = Flask(__name__)

    if os.environ.get('FLASK_ENV') == 'testing':
        app.config.from_object('test_config.TestConfigurations')
    elif os .environ.get('FLASK_ENV') == 'development':
        app.config.from_object('development_config.DevelopmentConfig')
    else:
        raise ValueError('FLASK_ENV inválido')

    db.init_app(app)
    Migrate(app, db)

    from project import urls
    urls.init_app(app)

    return app
