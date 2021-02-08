import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    @staticmethod
    def init_app(app):
        pass

class LocalConfig(Config):
    DEBUG = True
    CELERY_BROKER_URL = 'amqp://localhost//'
    CELERY_BACKEND = 'db+mysql://root:123456@localhost/celery'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost/celery'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    "local": LocalConfig}

SELECTED_CONFIG = "local"
