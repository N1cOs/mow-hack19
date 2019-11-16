from os import getenv

IS_DEV = True if getenv('APP_MODE') == 'DEV' else False


class Config:
    DEBUG = IS_DEV
