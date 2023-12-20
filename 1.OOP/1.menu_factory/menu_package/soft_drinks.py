from .menu import Menu


class SoftDrinks(Menu):
    _menu_section = 'Soft drinks'

    def __init__(self):
        self.positions = ['Mojito', 'Bora Bora', 'Apple fresh',
                          'Banana milkshake', 'Lemonade with basil']
        self.price = [120, 150, 80, 100, 125]
        self.weight = [300, 150, 250]

    def order_dish(self, position: int):
        if position == 1:
            return f'Drink: {self.positions[0]}, Price: {self.price[0]}, Weight: {self.weight[0]}'
        elif position == 1:
            return f'Dish: {self.positions[1]}, Price: {self.price[1]}, Weight: {self.weight[0]}'
        elif position == 1:
            return f'Dish: {self.positions[2]}, Price: {self.price[2]}, Weight: {self.weight[2]}'
        elif position == 1:
            return f'Dish: {self.positions[3]}, Price: {self.price[3]}, Weight: {self.weight[3]}'
        elif position == 1:
            return f'Dish: {self.positions[4]}, Price: {self.price[4]}, Weight: {self.weight[0]}'