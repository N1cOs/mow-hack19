import requests
import json
from app.model.official import Official

REGION_CACHE = {}

REGIONS = {
    "24": "Алтайский край",
    "33": "Амурская область",
    "37": "Архангельская область",
    "38": "Астраханская область",
    "96": "Белгородская область",
    "35": "Брянская область",
    "36": "Владимирская область",
    "41": "Волгоградская область",
    "42": "Вологодская область",
    "43": "Воронежская область",
    "93": "Еврейская автономная область",
    "44": "Забайкальский край",
    "99": "Ивановская область",
    "45": "Иркутская область",
    "9": "Кабардино-Балкарская Республика",
    "46": "Калининградская область",
    "97": "Калужская область",
    "48": "Камчатский край",
    "11": "Карачаево-Черкесская республика",
    "50": "Кемеровская область",
    "51": "Кировская область",
    "53": "Костромская область",
    "27": "Краснодарский край",
    "28": "Красноярский край",
    "98": "Курганская область",
    "55": "Курская область",
    "56": "Ленинградская область",
    "57": "Липецкая область",
    "58": "Магаданская область",
    "63": "Москва",
    "64": "Московская область",
    "65": "Мурманская область",
    "102": "Ненецкий автономный округ",
    "66": "Нижегородская область",
    "67": "Новгородская область",
    "68": "Новосибирская область",
    "69": "Омская область",
    "105": "Оренбургская область",
    "70": "Орловская область",
    "72": "Пензенская область",
    "29": "Пермский край",
    "74": "Приморский край",
    "75": "Псковская область",
    "3": "Республика Адыгея",
    "6": "Республика Алтай",
    "4": "Республика Башкортостан",
    "5": "Республика Бурятия",
    "59": "Республика Дагестан",
    "8": "Республика Ингушетия",
    "47": "Республика Калмыкия",
    "12": "Республика Карелия",
    "13": "Республика Коми",
    "109": "Республика Крым*",
    "61": "Республика Марий Эл",
    "62": "Республика Мордовия",
    "92": "Республика Саха (Якутия)",
    "17": "Республика Северная Осетия — Алания",
    "18": "Республика Татарстан",
    "85": "Республика Тува (Тыва)",
    "21": "Республика Хакасия",
    "76": "Ростовская область",
    "103": "Рязанская область",
    "77": "Самарская область",
    "1": "Санкт-Петербург",
    "79": "Саратовская область",
    "94": "Сахалинская область",
    "80": "Свердловская область",
    "110": "Севастополь*",
    "100": "Смоленская область",
    "81": "Ставропольский край",
    "82": "Тамбовская область",
    "101": "Тверская область",
    "106": "Томская область",
    "84": "Тульская область",
    "86": "Тюменская область",
    "20": "Удмуртская республика",
    "88": "Ульяновская область",
    "32": "Хабаровский край",
    "108": "Ханты-Мансийский автономный округ — Югра",
    "89": "Челябинская область",
    "90": "Чеченская республика",
    "91": "Чувашская республика - Чувашия",
    "95": "Чукотский автономный округ",
    "104": "Ямало-Ненецкий автономный округ",
    "107": "Ярославская область"
}


def get_official_info(person_id):
    person = get_person(person_id)
    name = person['family_name'] + ' ' + \
        person['name'] + ' ' + person['patronymic']
    sections = get_sections(name)
    declaration = sections['sections'][-1]['sections'][-1]

    total_income = 0
    incomes = declaration['incomes']
    for income in incomes:
        total_income += income['size']

    position = sections['sections'][-1]['position']
    #photo_url = get_photo(person_id)
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
    r = requests.get(
        'https://declarator.org/api/v1/search/person-sections/?name=' + str(name))
    data = json.loads(r.content)
    return data['results'][0]


def get_last_declaration(person_id):
    r = requests.get(
        'https://declarator.org/api/v1/search/sections/?person=' + str(person_id))
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
    r = requests.get('https://declarator.org/api/v1/search/sections/?page=' +
                     str(page) + '&region=' + str(region))
    data = json.loads(r.content)
    if 'results' in data:
        return data['results'][index % 10]
    return None


def get_declaration_count(region):
    r = requests.get(
        'https://declarator.org/api/v1/search/sections/?region=' + str(region))
    data = json.loads(r.content)
    return data['count']


def get_region(number):
    r = requests.get(
        'https://declarator.org/api/v1/search/sections/?region=' + str(number))
    data = json.loads(r.content)
    results = data['results']
    if results:
        return results[0]['main']['office']['region']['name']


def get_region_name(region):
    return REGIONS.get(str(region))


def _get_region_data(region):
    resp = REGION_CACHE.get(region)
    if resp is None:
        r = requests.get(
            'https://declarator.org/api/v1/search/sections/?region=' + str(region))
        resp = json.loads(r.content)
        REGION_CACHE[region] = resp

    return resp
