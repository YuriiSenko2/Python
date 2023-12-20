from datetime import datetime

# Return domains without a dot


def domains_editor(file_name):
    file = open(file_name, 'r')
    reading = file.read()
    edit = reading.replace('.', '')
    file.close()
    return list(edit.split())


result = domains_editor('domains.txt')
print(result)

# Return only second names


def second_names_search(file_name):
    file = open(file_name, 'r')
    second_name = [file.split()[4] for file in file.readlines()]
    return second_name


result = second_names_search('Names.txt')
print(result)

# Return a list with dictionaries that contain dates


def retrieve_date(file_name):
    date_list = []
    file = open(file_name, 'r')
    for line in file.readlines():
        lines = line.split("-")
        if len(lines) > 1:
            date = lines[0]
            day, month, year = date.split()
            dates = datetime.strptime(f"{day[:-2]} {month} {year}", "%d %B %Y")
            date_list.append(
                {
                    "date": date
                }
            )
    return date_list


print(retrieve_date("authors.txt"))


