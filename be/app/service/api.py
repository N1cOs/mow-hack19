import requests
import json
from app.model.official import Official


def get_official(region, declaration_index):
    declaration = get_declaration(region, declaration_index)
    person_id = declaration['main']['person']['id']
    name = declaration['main']['person']['name']
    person = get_person(name, region)
    declaration = person['sections'][-1]['sections'][-1]
    
    total_income = 0
    incomes = declaration['incomes']
    for income in incomes:
        total_income += income['size']
    
    position = person['sections'][-1]['position']
    photo_url = get_photo(person_id)
    declaration_url = 'https://declarator.org/person/' + str(person_id)
    region_name = get_region(region)

    return Official(person_id, photo_url, name, position, region_name, total_income, declaration_url)


def get_photo(person_id):
    r = requests.get('https://declarator.org/api/person/?id=' + str(person_id))
    data = json.loads(r.content)
    return data['results'][0]['photo']


def get_person(name, region):
    r = requests.get('https://declarator.org/api/v1/search/person-sections/?name=' + str(name) + '&region=' + str(region))
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