from .menu import Menu


class Desserts(Menu):
    _menu_section = 'Desserts'

    def __init__(self):
        self.positions = ['Trifle', 'Tiramisu', 'Chocolate fondant',
                          'Apple tart', 'Panacota']
        self.price = [90, 135, 115, 130, 100]
        self.weight = [150, 200, 180, 220, 150]

    def order_dish(self, position: int):
        if position == 1:
            return f'Dish: {self.positions[0]}, Price: {self.price[0]}, Weight: {self.weight[0]}'
        elif position == 2:
            return f'Dish: {self.positions[1]}, Price: {self.price[2]}, Weight: {self.weight[3]}'
        elif position == 3:
            return f'Dish: {self.positions[2]}, Price: {self.price[2]}, Weight: {self.weight[2]}'
        elif position == 4:
            return f'Dish: {self.positions[3]}, Price: {self.price[3]}, Weight: {self.weight[3]}'
        elif position == 5:
            return f'Dish: {self.positions[4]}, Price: {self.price[4]}, Weight: {self.weight[4]}'