from datetime import datetime
from datetime import timedelta

# A function that adds or subtracts a specific number of days from a particular date


def get_date(date, days, add=True):
    if add:
        return datetime.date(date) + timedelta(days)
    return datetime.date(date) - timedelta(days)


subtract_days = get_date(datetime(2023, 1, 1), 2, False)
add_days = get_date(datetime(2023, 1, 1), 2, True)
print(subtract_days, ';', add_days)

# A function that calculates the exact age of a person


def calculate_age(today, birth_date):
    return int((today.timestamp() - birth_date.timestamp()) / 31556952), birth_date.timestamp()


def birthDate():
    birth_year = int(input('Year of birth: '))
    birth_month = int(input('Month of birth: '))
    birth_day = int(input('Day of birth: '))
    return birth_year, birth_month, birth_day


year, month, day = birthDate()
result = calculate_age(datetime.now(), datetime(year, month, day))
print('Your age in years and seconds', result)






