import os

class Config(object):
    """
    Parent configuration class.
    """
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    DATABASE_URI = os.getenv('DATABASE_URL')


class DevelopmentConfig(Config):
    """
    Configurations for development.
    """
    DEBUG = True
    DATABASE_URL = 'postgres://postgres:lionelmessi10@localhost:5432/chat1_db'


class TestingConfig(Config):
    """
    Configurations for Testing, with a different database.
    """
    TESTING = True
    DATABASE_URL = 'postgres://postgres:lionelmessi10@localhost:5432/chat1_db'
    DEBUG = True


app_config = {
'development': DevelopmentConfig,
'testing': TestingConfig
}
