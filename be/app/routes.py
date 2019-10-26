import app.service.api as api
import app.service.inflation as inflation
import time
import logging
import re
import json
from app.app import app
from flask import request
from app.model.official import Official
from app.service.distribution import calculate_distribution
from random import randint
from flask import jsonify, g, abort

OFFICIALS = {}
ITEMS = {}
OPTIONS_REGEX = re.compile(r'^((\d+?(\s?[,\s]\s?))*?)(\d+)$')


def init():
    with open('app/tmp/officials.txt', 'r') as file:
        line = file.readline()
        while line != '':
            id, name, surname, patronymic, photo = line.split()
            name = f'{name} {surname} {patronymic}'
            OFFICIALS[int(id)] = Official(int(id), photo, name)
            line = file.readline()

    with open('app/tmp/items.json', 'r') as file:
        global ITEMS
        ITEMS = json.load(file)


@app.route('/official', methods=['GET'])
def official():
    prh_ids = request.args.get('ids')
    if prh_ids is None:
        prh_ids = []
    elif OPTIONS_REGEX.match(prh_ids.strip()):
        prh_ids = prh_ids.split(',')
        prh_ids = [int(i.strip()) for i in prh_ids]
    else:
        abort(400)

    ids = [i for i in OFFICIALS if i not in prh_ids]
    id = ids[randint(0, len(ids) - 1)]
    official = OFFICIALS[id]

    pos, region, income, year, declaration_url = api.get_official_info(id)
    income = inflation.calc_inflation(income, year)
    official.position = pos
    official.regionName = region
    official.income = round(income)
    official.incomeStr = f'{official.income:,}'
    official.year = year
    official.declarationUrl = declaration_url

    return jsonify(vars(official))


@app.route('/item', methods=['GET'])
def item():
    income = request.args.get('income')
    if income is None:
        abort(400)
    else:
        income = int(income)

    items = calculate_distribution(income, ITEMS)
    resp, total_sum = {'items': []}, 0
    for item in items:
        resp['items'].append(vars(item))
        total_sum += item.full_price

    total_sum = round(total_sum)
    resp['totalSum'] = total_sum
    resp['totalSumStr'] = f'{total_sum:,}'

    return jsonify(resp)


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
