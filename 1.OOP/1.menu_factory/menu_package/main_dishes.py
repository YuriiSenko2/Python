from .menu import Menu


class MainDishes(Menu):
    _menu_section = 'Main Dishes'

    def __init__(self):
        self.positions = ['Beef Wellington', 'Fish and chips', 'Paella',
                          'Coq au vin', 'Tournedos Rossini']
        self.price = [550, 160, 200, 320, 650]
        self.weight = [300, 400, 300, 330, 350]

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
            return f'Dish: {self.positions[4]}, Price: {self.price[4]}, Weight: {self.weight[4]}'