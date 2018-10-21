# services/users/project/config.py

import os

class BaseConfig:
    """Base Configuration"""
    TESTING = False
    SQLALECHMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')

class ProductionConfig(BaseConfig):
    """Production environment"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')