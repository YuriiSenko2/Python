from random import randint
from functools import reduce

# Find intersections of two arrays

list_1_content = input('Add value to the list 1: ')
list_1 = []

while list_1_content != 'Next list':
    list_1.append(list_1_content)
    list_1_content = input('Add value to the list 1: ')

list_2_content = input('Add value to the list 2: ')
list_2 = []

while list_2_content != 'Finish':
    list_2.append(list_2_content)
    list_2_content = input('Add value to the list 2: ')

out = list(filter(lambda intersection: intersection in list_1, list_2))
print(out)

# Find out if the string is digit

new_string = input()
ifNumber = lambda x: True if x.isdigit() else False
print(ifNumber(new_string))

# Find the longest and shortest lists

list_1 = ['Kharkiv', 1, 'Dnipro', 'Kherson']
list_2 = ['Poltava', 3, 4]
list_3 = ['Ternopil', 'Lviv', 'Mykolaiv', 'Kyiv', 'Chernivtsi']
max_list = max(list_1, list_2, list_3, key=lambda longest: len(longest))
min_list = min(list_1, list_2, list_3, key=lambda shortest: len(shortest))
print(max_list, min_list, sep='\n')

# Product of all numbers

numbers = []
for a in range(5):
    numbers.append(randint(1, 5))
print(numbers)
numbers_product = reduce(lambda x, y: x * y, numbers)
print(numbers_product)