# 1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Persian(Cat):
    def sing(self, sounds):
        return f'{sounds}'


if __name__ == '__main__': # ran it here again to be more organized
    cat1 = Chartreux('joey', 5)
    cat2 = Chartreux('Tom', 9)
    cat3 = Chartreux('Luey', 7)

    my_cats = [cat1, cat2, cat3]

    my_pets = Pets(my_cats)
    my_pets.walk()

# 2

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking ouff!!'

    def run_speed(self):
        speed = self.weight/self.age*10
        return f'{self.name} is runing at {speed} km/h', speed

    def fight(self, other_dog):
        if self.run_speed()[1] > other_dog.run_speed()[1]:
            return f'{self.name} won!!'
        else:
            return f'{other_dog.name} won!!'


if __name__ == '__main__':
    dog1 = Dog('lucky', 4, 15)
    dog2 = Dog('joey', 3, 13)
    dog3 = Dog('sss', 9, 4)
    print(dog1.bark())
    print(dog1.fight(dog2))


