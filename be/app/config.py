from os import getenv


class Config:
    DEBUG = True

    DB_USER = getenv('DB_USER')
    DB_PASSWORD = getenv('DB_PASSWORD')

    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/items'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
