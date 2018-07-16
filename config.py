import os


class Configuration:
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    # SQLALCHEMY_DATABASE_URL = 'postgresql://localhost/postgres_db'
    DEBUG = True
