class Item:
    def __init__(self, level, item_name, item_unit, item_count, full_price):
        self.full_price = full_price
        self.item_count = item_count
        self.item_unit = item_unit
        self.item_name = item_name
        self.level = level

    