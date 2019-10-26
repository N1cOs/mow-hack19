import requests
import json
from app.model.official import Official

REGION_CACHE = {}


def get_official_info(person_id):
    person = get_person(person_id)
    name = person['family_name'] + ' ' + person['name'] + ' ' + person['patronymic']
    sections = get_sections(name)
    declaration = sections['sections'][-1]['sections'][-1]

    total_income = 0
    incomes = declaration['incomes']
    for income in incomes:
        total_income += income['size']

    position = sections['sections'][-1]['position']
    photo_url = get_photo(person_id)
    declaration_url = 'https://declarator.org/person/' + str(person_id)
    year = declaration['main']['year']

    if declaration['main']['office']['region']:
        region = declaration['main']['office']['region']['id']
    else:
        region = None
    region_name = get_region_name(region)

    return position, region_name, total_income, year, declaration_url


def get_person(person_id):
    r = requests.get('https://declarator.org/api/person/?id=' + str(person_id))
    data = json.loads(r.content)
    return data['results'][0]


def get_photo(person_id):
    r = requests.get('https://declarator.org/api/person/?id=' + str(person_id))
    data = json.loads(r.content)
    return data['results'][0]['photo']


def get_sections(name):
    r = requests.get('https://declarator.org/api/v1/search/person-sections/?name=' + str(name))
    data = json.loads(r.content)
    return data['results'][0]


def get_last_declaration(person_id):
    r = requests.get('https://declarator.org/api/v1/search/sections/?person=' + str(person_id))
    data = json.loads(r.content)
    index = data['count'] - 1
    if index > 9:
        page = int(index / 10 + 1)
        r = requests.get(
            'https://declarator.org/api/v1/search/sections/?page=' + str(page) + '&person=' + str(person_id))
        data = json.loads(r.content)
        index = index % 10
    return data['results'][index]


def get_declaration(region, index):
    page = int(index / 10 + 1)
    r = requests.get('https://declarator.org/api/v1/search/sections/?page=' + str(page) + '&region=' + str(region))
    data = json.loads(r.content)
    if 'results' in data:
        return data['results'][index % 10]
    return None


def get_declaration_count(region):
    r = requests.get('https://declarator.org/api/v1/search/sections/?region=' + str(region))
    data = json.loads(r.content)
    return data['count']


def get_region(number):
    r = requests.get('https://declarator.org/api/v1/search/sections/?region=' + str(number))
    data = json.loads(r.content)
    results = data['results']
    if results:
        return results[0]['main']['office']['region']['name']


def get_region_name(region):
    return region


def _get_region_data(region):
    resp = REGION_CACHE.get(region)
    if resp is None:
        r = requests.get('https://declarator.org/api/v1/search/sections/?region=' + str(region))
        resp = json.loads(r.content)
        REGION_CACHE[region] = resp
    
    return resp