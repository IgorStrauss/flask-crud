from flask import Config


class DevelopmentConfig(Config):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATION = False
    SECRET_KEY = 'asdklj23476hkjda'
