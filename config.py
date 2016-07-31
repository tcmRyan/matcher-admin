import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Configuration to be loaded into the heroku environment
    DO NOT CHECK IN
    """
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ['SECRET_KEY']

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True