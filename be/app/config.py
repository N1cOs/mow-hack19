from os import getenv

IS_DEV = True if getenv('APP_MODE') == 'DEV' else False


class Config:
    DEBUG = IS_DEV 

    DB_USER = getenv('DB_USER')
    DB_PASSWORD = getenv('DB_PASSWORD')

    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/items'
    SQLALCHEMY_ECHO = IS_DEV
    SQLALCHEMY_TRACK_MODIFICATIONS = False
