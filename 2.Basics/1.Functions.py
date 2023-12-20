from random import choice, randint
from string import ascii_letters

# Count the area of the rectangle and inform if it's a square.


def isRectangle(side_a, side_b, side_c, side_d) -> int:
    if (side_a ** 2) + (side_b ** 2) == (side_c ** 2) + (side_d ** 2) and side_a != side_b:
        return True
    return False


def rectangle_square(side_a, side_b) -> int:
    result = side_a * side_b
    return result


def isSquare(side_a, side_b, side_c, side_d) -> int:
    if side_a == side_b == side_c == side_d:
        return True
    return False


def side_size():
    while True:
        try:
            side1 = int(input('Value of the side 1: '))
            side2 = int(input('Value of the side 2: '))
            side3 = int(input('Value of the side 3: '))
            side4 = int(input('Value of the side 4: '))
            return side1, side2, side3, side4
        except ValueError:
            print('Only digits are allowed, start over!')


side_1, side_2, side_3, side_4 = side_size()

if isRectangle(side_1, side_2, side_3, side_4):
    s = rectangle_square(side_1, side_2)
    print(s)
elif isSquare(side_1, side_2, side_3, side_4):
    print('Square')
else:
    print('Neither rectangle nor square')

# Random email creator


def random_email():
    list_addition = input('Enter the name: ')
    names = []
    while list_addition != 'stop':
        if list_addition.isalpha():
            names.append(list_addition)
        else:
            print('Only letters are allowed')
        list_addition = input('Enter the name: ')
    domains = ['net', 'com', 'ua']
    return f"{choice(names)}." \
           f"{randint(100,999)}@" \
           f"{''.join(choice(ascii_letters) for _ in range(randint (5,7)))}." \
           f"{choice(domains)}"


result = random_email()
print(result)

