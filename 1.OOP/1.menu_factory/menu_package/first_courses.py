from .menu import Menu


class FirstCourses(Menu):
    _menu_section = 'First courses'

    def __init__(self):
        self.positions = ['Bouillabaisse', 'French onion soup', 'Minestrone',
                          'Mushroom cream soup', 'Manhattan clem chowder']
        self.price = [310, 220, 170, 240, 290]
        self.weight = [350, 280, 300, 340]

    def order_dish(self, position: int):
        if position == 1:
            return f'Dish: {self.positions[0]}, Price: {self.price[0]}, Weight: {self.weight[0]}'
        elif position == 2:
            return f'Dish: {self.positions[1]}, Price: {self.price[1]}, Weight: {self.weight[1]}'
        elif position == 3:
            return f'Dish: {self.positions[2]}, Price: {self.price[2]}, Weight: {self.weight[2]}'
        elif position == 4:
            return f'Dish: {self.positions[3]}, Price: {self.price[2]}, Weight: {self.weight[3]}'
        elif position == 5:
            return f'Dish: {self.positions[4]}, Price: {self.price[4]}, Weight: {self.weight[4]}'