"""
Controls the configuration for all the different deployments of this
application
"""

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Configuration to be loaded into the heroku environment
    DO NOT CHECK IN
    """
    DEBUG = False
    CSRF_ENABLED = True
    WTF_CSRF_ENABLED = True
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    """
    Configuration for the Production Environment
    """
    DEBUG = False


class DevelopmentConfig(Config):
    """
    Configuration for development environments
    """
    DEBUG = True
    