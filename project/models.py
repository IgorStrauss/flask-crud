from datetime import datetime

import pytz
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(35), unique=True, nullable=False)
    email = db.Column(db.String(45), unique=True, nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.now, server_default=db.func.now())

    def __str__(self):
        return self.first_name

    @property
    def format_date(self):
        local_tz = pytz.timezone('America/Sao_Paulo')
        return self.created_at.astimezone(local_tz).strftime(
            '%d/%m/%Y - %H:%M')
