import app.service.api as api
import time
import logging
from app.app import app
from flask import request
from app.model.official import Official
from random import randint
from flask import jsonify, g

OFFICIALS = {}


def init():
    with open('app/tmp/officials.txt') as file:
        line = file.readline()
        while line != '':
            id, name, surname, patronymic, photo = line.split()
            name = f'{name} {surname} {patronymic}'
            OFFICIALS[id] = Official(id, photo, name)
            line = file.readline()


@app.route('/official', methods=['GET'])
def official():
    return 'official'


@app.route('/item', methods=['GET'])
def item():
    return 'item'


@app.before_request
def pre_handler():
    g.start = time.time()


@app.after_request
def post_handler(response):
    duration = round((time.time() - g.start) * 1000)
    msg = f'[{request.method} {request.path}] [{duration}ms] {response.status}'
    logging.info(msg)

    return response


init()
