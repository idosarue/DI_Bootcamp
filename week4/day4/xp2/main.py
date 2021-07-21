# 7
from datetime import datetime
today = datetime.today()


def get_age():
    date = input('enter your birth date in dd/mm/yyyy format: ')
    birth_date = datetime.strptime(date, "%d/%m/%Y")
    age = int(((today - birth_date).days / 365))
    return age


def get_gender():
    gender = input('What is your gender m/f? ')
    return gender


def can_retire(gender, age):
    if gender == 'm':
        retirement_age = 67
        if age >= retirement_age:
            return 'can retire'
        else:
            return 'can\'t'
    else:
        retirement_age = 62
        if age >= retirement_age:
            return 'can retire'
        else:
            return 'can\'t'


print(can_retire(get_gender(), get_age()))


# 8
#  X+XX+XXX+XXXX.
def calc(x):
    sum_of_xs = x + (x * 11) + (x * 111) + (x * 1111)
    return sum_of_xs


print(calc(3))