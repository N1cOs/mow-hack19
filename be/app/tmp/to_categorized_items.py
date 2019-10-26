import json
import os


class Item:
    def __init__(self, *args, **kwargs):
        name = kwargs['name']
        unit = kwargs['unit']
        price = kwargs['price']
        
        self.name = name
        self.unit = unit
        self.price = price
    
    def __eq__(self, other):
        return self.price == other.price
    
    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price


def join_with_pwd(filepath):
    return os.path.join(os.path.dirname(__file__), filepath)


def split_by_proportion(list, proportions):
    items_taken = 0
    split_list = []
    for prop in proportions:
        is_last_prop = proportions.index(prop) == len(proportions) - 1
        items_num = len(list) if is_last_prop else int(len(list) * prop)
        split_list.append(list[items_taken : items_taken + items_num])
        items_taken += items_num
    return split_list


items = []
with open(join_with_pwd('uncategorized_items.json'), 'r') as file:
    data = json.load(file)
    for item in data:
        temp = item['name']
        if temp.find(',') != -1:
            name, unit = temp.split(',')
        else:
            name, unit = temp, ''
        price = item['price']
        if isinstance(price, str):
            price = price
            price = float(price.replace(' ', '').replace(',', '.'))
        else:
            price = float(price)

        item = Item(name=name, unit=unit, price=price)
        items.append(item)

items.sort(key=lambda a: a.price, reverse=True)

proportions = [0.1, 0.3, 0.6] # hardcoded
categories = split_by_proportion(items, proportions)
result = {str(j + 1): [vars(i) for i in sorted(categories[j], reverse=True)] for j in range(len(proportions))}

with open(join_with_pwd('items.json'), 'w') as file:
    data = json.dumps(result, ensure_ascii=False)
    file.write(data)
