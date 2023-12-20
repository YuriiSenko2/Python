from menu_package.menu import Menu
from menu_package.appetizers import Appetizers
from menu_package.salads import Salads
from menu_package.first_courses import FirstCourses
from menu_package.main_dishes import MainDishes
from menu_package.desserts import Desserts
from menu_package.soft_drinks import SoftDrinks
from menu_package.alcohol import Alcohol
import datetime


class MenuFactory:
    def __init__(self):
        self.sections_number = 7
        self.menu_creator = 'Hector Himenez-Bravo'

    def get_section(self, section: int) -> Menu:
        if section == 1:
            return Appetizers()
        elif section == 2:
            return Salads()
        elif section == 3:
            return FirstCourses()
        elif section == 4:
            return MainDishes()
        elif section == 5:
            return Desserts()
        elif section == 6:
            return SoftDrinks()
        elif section == 7:
            return Alcohol()
        else:
            raise AttributeError('Only digits from 1 to 7 are allowed')


class DailyReport:
    def __init__(self, date: str):
        self.date = date
        self.all_receipts = dict()

    def set_time(self, year, month, day, hours, minutes, seconds):
        t = datetime.datetime(year=year, month=month, day=day, hour=hours, minute=minutes, second=seconds)
        return f'Time: {t.day}/{t.month}/{year} {hours}:{minutes}:{seconds}'

    def __setitem__(self, key, value):
        self.all_receipts[key] = value

    def __getitem__(self, item):
        return self.all_receipts[item]


order1 = MenuFactory()
section1 = order1.get_section(2)
position1 = section1.order_dish(3)
section2 = order1.get_section(4)
position2 = section2.order_dish(2)
position3 = section2.order_dish(5)

order2 = MenuFactory()
section2_1 = order2.get_section(1)
position2_1 = section2_1.order_dish(4)
section2_2 = order2.get_section(3)
position2_2 = section2_2.order_dish(1)
position2_3 = section2_1.order_dish(5)
section2_4 = order2.get_section(7)
position2_4 = section2_4.order_dish(1)

checks = DailyReport('04.10.2023')
order_time1 = checks.set_time(2023, 10, 4, 12, 39, 10)
checks[1] = position1, position2, position3, order_time1
for el in checks[1]:
    print(el)
print('-----------------------------------------------------------------------------------------------------------')
order_time2 = checks.set_time(2023, 10, 4, 13, 11, 14)
checks[2] = position2_1, position2_2, position2_3, position2_4, order_time2
for el in checks[2]:
    print(el)