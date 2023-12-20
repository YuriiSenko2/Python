from random import randrange
from random import randint

# Determining the quarter containing the random number

minutes = randrange(60)
if minutes <= 15:
    print('first quarter')
elif minutes <= 30:
    print('second quarter')
elif minutes <= 45:
    print('third quarter')
else:
    print('fourth quarter')

# Determining the characteristic corresponding to the month of the birth

birth_month = int(input('Your birth month: '))
winter_months = [1, 2, 12]
spring_months = [3, 4, 5]
summer_months = [6, 7, 8]
autumn_months = [9, 10, 11]
if birth_month in winter_months:
    print('Snow was drifting past the window')
elif birth_month in spring_months:
    print('Everything around was blooming')
elif birth_month in summer_months:
    print('Kids were enjoying the summer break')
elif birth_month in autumn_months:
    print('Everything around was flashing with bright colors')
else:
    print('Wrong month. \nTry something from 1 to 12.')

# Determining if the number is divisible by 6

num = randint(-2147483648, 2147483647)
amount = 0
digit = (num // 10 ** 0) % 10
while num != 0:
    last_digit = num % 10
    amount = amount + last_digit
    num = num // 10
if amount % 3 == 0 == digit % 2:
    print('Entered number is divisible by 6')
else:
    print('Entered number is not divisible by 6')

# Determining the quarter containing the point

x = float(input('x = '))
y = float(input('y = '))
if x > 0 < y:
    print('Point is in the first quarter')
elif x < 0 < y:
    print('Point is in the second quarter')
elif x < 0 > y:
    print('Point is in the third quarter')
elif x < 0 > y:
    print('Point is in the fourth quarter')
elif x == 0 == y:
    print('Point is at the origin')
elif x == 0 and y > 0 or y < 0:
    print('Point is on the y-axis')
else:
    print('Point is on the x-axis')








