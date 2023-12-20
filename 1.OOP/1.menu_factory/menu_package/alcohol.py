from .menu import Menu


class Alcohol(Menu):
    _menu_section = 'Alcoholic beverages'

    def __init__(self):
        self.positions = ['Hankey Banister', 'Bacardi', 'Courvoisier VSOP',
                          'Finlandia redberry', 'Stella Artois']
        self.price = [800, 750, 4500, 600, 90]
        self.weight = [500]

    def order_dish(self, position: int):
        if position == 1:
            return f'Drink: {self.positions[0]}, Price: {self.price[0]}, Weight: {self.weight[0]}'
        elif position == 2:
            return f'Drink: {self.positions[1]}, Price: {self.price[1]}, Weight: {self.weight[0]}'
        elif position == 3:
            return f'Drink: {self.positions[2]}, Price: {self.price[2]}, Weight: {self.weight[0]}'
        elif position == 4:
            return f'Drink: {self.positions[3]}, Price: {self.price[3]}, Weight: {self.weight[0]}'
        elif position == 5:
            return f'Drink: {self.positions[4]}, Price: {self.price[4]}, Weight: {self.weight[0]}'