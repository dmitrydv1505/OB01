class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price


# Создаем магазины
store1 = Store("Магазин овощей и фруктов", "ул. Ленина, 1")
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

store2 = Store("Магазин текстиля", "ул. Пушкина, 5")
store2.add_item("t-shirts", 10)
store2.add_item("pants", 15)

store3 = Store("Аптека", "пр. Победы, 10")
store3.add_item("painkillers", 3)
store3.add_item("band-aids", 1)

# Тестируем методы
print(store1.items)  # {'apples': 0.5, 'bananas': 0.75}
store1.update_price("apples", 0.6)
print(store1.get_price("apples"))  # 0.6

store1.remove_item("bananas")
print(store1.items)  # {'apples': 0.6}
print(store1.get_price("bananas"))  # None
