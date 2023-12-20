# Find all repeating numbers and print them in ascending order

list_1 = set([16, 23, 20, 28, 2, 4, 8, 19, 17, 10, 9])
list_2 = set([99, 19, 22, 13, 2, 79, 21, 68, 10, 8, 9])
duplicate_values = list_1 & list_2
print(duplicate_values)

# Determine the average score and print students with above average performance

student_rating = {
    'Mike': 100,
    'Davide': 66,
    'Malik': 90,
    'Pierre': 89,
    'Fikayo': 78,
    'Theo': 95,
    'Tidjani': 77,
    'Ismael': 100,
    'Rafael': 90,
    'Samuel': 70,
    'Olivier': 85
}

average_score = sum(student_rating.values())/len(student_rating)
average_score = average_score.__round__(1)
print(average_score)

for element in student_rating:
    if student_rating[element] > average_score:
        print(element)

# Amount of different numbers

integers = [16, 23, 20, 28, 2, 4, 8, 19, 17, 10, 9, 99, 19, 22, 13, 2, 79, 21, 68, 10, 8, 9]
diff_numbers = set(integers)
print(len(diff_numbers))

# Find all repeating numbers and print them in ascending order on separate lines

numbers = input('Enter a number in the first list: ')
first_list = []

while numbers != 'Second list':
    numbers = int(numbers)
    first_list.append(numbers)
    numbers = input('Enter a number in the first list: ')

numbers_2 = input('Enter a number in the second list: ')
second_list = []

while numbers_2 != 'Stop':
    numbers_2 = int(numbers_2)
    second_list.append(numbers_2)
    numbers_2 = input('Enter a number in the second list: ')

filter_1 = set(first_list)
filter_2 = set(second_list)
filter_3 = filter_1.intersection(filter_2)
new_list = list(filter_3)
new_list.sort()

for element in new_list:
    print(element)


