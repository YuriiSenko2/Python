keywords = ['False', 'True', 'None', 'and', 'with', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
            'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
            'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

# Create a new list with deleted first symbol for all items

new_keyword = [i[1:] for i in keywords]
print(new_keyword)

# Create a list with the length of each item

length = [len(i) for i in keywords]
print(length)

# Create a list that contains only words with five or more symbols

words = [i for i in keywords if len(i) >= 5]
print(words)

# Create a list that contains squares of numbers from 1 to input

squares = [i ** 2 for i in range(1, int(input()) + 1)]
print(*squares, sep='\n')

# Select only digits from the text

only_digits = [i for i in input() if i.isdigit()]
print(*only_digits, sep=' ')

# Create a list with only even numbers in the range from 0 to input

only_even = [i for i in range(int(input()) + 1) if i % 2 == 0 and i != 0]
print(only_even)

# Create a list with a sum of values that are in equal positions in each string

string1, string2 = input().split(), input().split()
the_sum = [(int(string1[i]) + int(string2[i])) for i in range(len(string1))]
print(*the_sum)

# Find the longest word in a list

catalogue = [len(i) for i in input().split()]
print(max(catalogue))
