import logging
from flask import Flask

from app.config import Config
from sys import stdout

app = Flask(__name__)
app.config.from_object(Config)

logging.basicConfig(stream=stdout, level=logging.INFO)
