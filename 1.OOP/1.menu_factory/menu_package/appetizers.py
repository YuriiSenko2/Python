from .menu import Menu


class Appetizers(Menu):
    _menu_section = 'Appetizers'

    def __init__(self):
        self.positions = ['Guacamole with corn chips', 'Wild mushrooms pate', 'Vitello tonnato',
                          'Shrimp vol-au-vent', 'Goat cheese balls']
        self.price = [120, 130, 230, 180, 90]
        self.weight = [150, 100, 110, 150]

    def order_dish(self, position: int):
        if position == 1:
            return f'Dish: {self.positions[0]}, Price: {self.price[0]}, Weight: {self.weight[0]}'
        elif position == 2:
            return f'Dish: {self.positions[1]}, Price: {self.price[1]}, Weight: {self.weight[1]}'
        elif position == 3:
            return f'Dish: {self.positions[2]}, Price: {self.price[2]}, Weight: {self.weight[2]}'
        elif position == 4:
            return f'Dish: {self.positions[3]}, Price: {self.price[3]}, Weight: {self.weight[3]}'
        elif position == 5:
            return f'Dish: {self.positions[4]}, Price: {self.price[4]}, Weight: {self.weight[1]}'