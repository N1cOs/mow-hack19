import app.service.api as api
import time
import logging
from app.app import app
from flask import request
from random import randint
from flask import jsonify, g


@app.route('/official', methods=['GET'])
def official():
    region = request.args.get('region')
    if region is None:
        region = '77'

    count = api.get_declaration_count(region)
    off_id = randint(0, count)

    return jsonify(vars(api.get_official(region, off_id)))


@app.before_request
def pre_handler():
    g.start = time.time()


@app.after_request
def post_handler(response):
    duration = round((time.time() - g.start) * 1000)
    msg = f'[{request.method} {request.path}] [{duration}ms] {response.status}'
    logging.info(msg)

    return response
