import csv

# 1. Create a function that reads a CSV file
# 2. Create a function that writes data to a file in a CSV format
# 3. Using the created functions:
# a) create and read a file and then add lines into a variable
# b) add two new lines into a variable
# c) write changes into another file


def file_reader(file_name):
    with open(file_name, 'r') as csv_reader:
        reading = csv.reader(csv_reader)
        return list(reading)


def file_writer(file_name, listing):
    to_add = listing
    with open(file_name, 'w', newline='') as csvf:
        file = csv.writer(csvf)
        for row in to_add:
            file.writerow(row)


file_writer('catalogue.csv', [['Surname', 'Team', 'Number'], ['Maignan', 'AC Milan', 16],
                           ['Ramsdale', 'Arsenal', 1]])

strings = file_reader('catalogue.csv')
print(strings)
strings.append(['Tomori', 'AC Milan', 23])
strings.append(['Gaya', 'Valencia', 14])

file_writer('new_catalogue.csv', strings)
print(file_reader('new_catalogue.csv'))


