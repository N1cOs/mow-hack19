import logging
from flask import Flask

from app.config import Config
from sys import stdout
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

logging.basicConfig(stream=stdout, level=logging.INFO)
