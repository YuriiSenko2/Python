class PetShop:
    def __init__(self, animal: str = None, breed: str = None, price: int = None, quantity: int = None):
        self.__animal = animal
        self.__breed = breed
        self.__price = price
        self.__quantity = quantity

    @property
    def animal(self):
        return self.__animal

    @property
    def breed(self):
        return self.__breed

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @animal.setter
    def animal(self, value):
        self.__animal = value

    @breed.setter
    def breed(self, value):
        self.__breed = value

    @price.setter
    def price(self, value):
        self.__price = value

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    @staticmethod
    def more_than_one(quantity, price):
        return quantity * price


order_1 = PetShop('Dog', 'pug', 1000, 1)
print(order_1.quantity)
order_1.quantity = 3
print(order_1.quantity)
order_1.price = order_1.more_than_one(order_1.price, order_1.quantity)
print(order_1.price)
