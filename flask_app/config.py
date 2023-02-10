import pathlib
import os


# Flask config class
class Config(object):
    TESTING = False
    SECRET_KEY = 'GF9NWEgxdS51WEGNX6vsng'
    # Uses memory, not needed in this case
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(pathlib.Path(__file__).parent.joinpath('flask_app_db.sqlite3'))
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('COMP0045.reset@gmail.com')
    MAIL_PASSWORD = os.getenv('test123test')
    POSTS_PER_PAGE = 10


class ProductionConfig(Config):

    pass


class DevelopmentConfig(Config):

    SQLALCHEMY_ECHO = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(pathlib.Path(__file__).parent.joinpath('flask_app_db.sqlite'))


class TestingConfig(Config):
    TESTING = True

    SQLALCHEMY_ECHO = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(pathlib.Path(__file__).parent.joinpath('flask_app_db.sqlite'))
