# 1
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat('Jerry', 22)
cat2 = Cat('Tom', 11)
cat3 = Cat('Leo', 7)

list_of_cats = [cat1, cat2, cat3]


def oldest_cat():
    max_age = max(cat1.age, cat2.age, cat3.age)
    for cat in list_of_cats:
        if max_age == cat.age:
            return f'The oldest cat is {cat.name}, and is {max_age} years old'


print(oldest_cat())


# 2

class Dog:
    def __init__(self, name, height=23):
        self.name = name
        self.height = height

    def bark(self):
        print(f'{self.name} goes woof!')

    def jump(self):
        print(f'{self.name} jumps {self.height * 2} cm high!') if type(self.height) == int else print(f'{self.height} is not a num')

    def details(self):
        print(self.name, self.height)
    
    def actions(self):
        self.jump()
        self.bark()

davids_dog = Dog('rex', 22)
davids_dog.details()
davids_dog.actions()

sarahs_dog = Dog('Teacup', 23)
sarahs_dog.details()
sarahs_dog.actions()

bigger_dog = sarahs_dog.name if sarahs_dog.height > davids_dog.height else davids_dog.name
print(bigger_dog)


# 3

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"]).sing_me_a_song()


# 4
from itertools import groupby
from operator import itemgetter

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:     
            self.animals.append(new_animal)
        else:
            print(f'{new_animal} already exists')
    
    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print(f'{animal_sold} not in zoo')

    def sort_animals(self):
        new_dict = {}
        self.animals.sort()
        x = [list(word) for letter, word in groupby(self.animals, key=itemgetter(0))]
        for index, word in enumerate(x):
            if len(word) < 2:
               word = "".join(word)
            new_dict[index + 1] = word
        print(new_dict)
        return new_dict
    
    def get_groups(self):
        d = self.sort_animals()
        for animal in d.values():
            print(animal)


ramat_gan_safari = Zoo('Ramat gan')
ramat_gan_safari.add_animal('monkey')
ramat_gan_safari.add_animal('tiger')
ramat_gan_safari.add_animal('goose')
ramat_gan_safari.add_animal('snake')
ramat_gan_safari.add_animal('epple')
ramat_gan_safari.add_animal('elephant')
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal('monkey')
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()