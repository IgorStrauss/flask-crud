from datetime import datetime

import pytest

from project import create_app
from project.models import User, db


@pytest.fixture(scope='session')
def app():
    app = create_app('testing')
    app_context = app.app_context()
    app_context.push()

    yield app

    app_context.pop()


@pytest.fixture(scope='session')
def client(app):
    return app.test_client()


@pytest.fixture(scope='session')
def database(app):
    db.create_all()

    user = User(
        first_name='admin-name',
        last_name='admin-lastname',
        username='admin-username',
        email='admin@email.com',
        created_at=datetime.now()
    )
    db.session.add(user)
    db.session.commit()

    yield db

    db.drop_all()
