import random
from app.model.item import Item


def calculate_distribution(income, data):
    # set limit
    direction = random.random() - 0.5 > 0
    if direction:
        income = income * (random.random() + 1)
    else:
        income = income * (0.5 + random.random() * 0.5)

    out_items = []
    # check levels
    for level_index in data:
        level = data[level_index]
        if level[-1]['price'] >= income:
            continue

        item_index = random.randrange(0, len(level))
        while level[item_index]['price'] >= income:
            item_index = random.randrange(item_index + 1, len(level))

        item = level[item_index]
        item_count = int(income / item['price'])
        full_price = item_count * item['price']
        income -= full_price

        out_items.append(Item(
            int(level_index), item['name'], item['unit'], item_count, round(full_price)))

    return out_items
