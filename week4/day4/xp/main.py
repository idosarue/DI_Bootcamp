import random


# 1
from typing import Any, Callable


def display_message():
    print('I\'m learning python')


display_message()


# 2
def favorite_book(title='The Catcher in the Rye'):
    print(f'One of my favorite books is {title}')


favorite_book('Alice in Wonderland')

x = lambda title: f'One of my favorite books is {title}'
print(x('Alice in Wonderland'))


# 3
def describe_city(city, country='Thailand'):
    print(f'{city} is in {country}')


describe_city('Bangkok')

city_lam = lambda city, country: f'{city} is in {country}'
print(city_lam('Tel Aviv', 'israel'))


# 4
def compare(num):
    if 1 <= num <= 100:
        random_num = random.randint(1, 100)
        if num == random_num:
            return 'success!'
        else:
            return f'Fail! {num} and {random_num} are not the same'
    else:
        return 'invalid number'


print(compare(100))


# 5
def make_shirt(size ="L", text="I love Python"):
    print(f'The shirt size is {size} it\'s text is {text} ')


make_shirt()
make_shirt("M")
make_shirt("s", 'small shirt')


def make_shirt(**kwargs):
    for key, value in kwargs.items():
        print(f'The shirt {key} is {value}')


make_shirt(size="L", text="Heloooo")


# 6
magicians_li = ['Merlin', 'ZOVELLO', 'LUNG TCHANG YUEN']


def show_magicians():
    for name in magicians_li:
        print(name)


show_magicians()


def make_great(magicians):
    for index, name in enumerate(magicians):
        magicians[index] += ' The greatest'
    return magicians


make_great(magicians_li)
print(magicians_li)

magicians_li2 = ['Merlin', 'ZOVELLO', 'LUNG TCHANG YUEN']


def make_great2(magicians):
    return magicians + " The greatest"


# map_object = list(map(make_great2, magicians_li2))
map_object2 = list(map(lambda n: n + " the greatest", magicians_li2))
print(map_object2)