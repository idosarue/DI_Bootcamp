# 1
"""
A class is a blueprint that is used in order to create objects.

An isntance is as an object created from a class

Encapsulation is a term for wrapping data and the methods used on that data in one unit. this prevents accidental change to the data.

Abstraction is a term for using everyday things(coffe machine, drone modules in code etc...) and not knowing how they work, just knowing that they work and what do they do.

Inheritance is for example:
a class of Cat that inherits it's attributes from a parent class Animal, an animal has legs a name a voice etc.. and the Cat class will get those attribute too

Multiple inheritance is for example:
a class of alien dog(like from one of the examples), the class inherites both from the Dog class and The alien class

Polymorphism is a concept that refers to a use of a single type entity inmultiple ways, for example:
the + operator can be used to add 2 numbers(1 + 2), it can also be used to concatenate strings("hello"+ " " + "world")
multiple classes can have the same method:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def run(self):
        print("a person runs at approx 15 km\h")
class Child(person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.name = name
        self.age = age
    def run(self):
        print("a child runs at approx 7 km\h")

MRO:
(taken from zero to mastery class.)
class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass

      A
    /   \
   /     \
  B       C
  \       /
   \     /
      D  
d inherits from B and C 
B, C inherit from A
so if we print num of D print(D.num), we will get 1
because it doesn't go from D to B and directly to A
it goes from D to B to C and finally to A

"""
import random
# 2
suit_li = ["Hearts", "Diamonds", "Clubs", "Spades"]
value_li = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for value in value_li for suit in suit_li] 
    
    def shuffle(self):
        random.shuffle(self.cards)
        for card in self.cards:
            print(card.suit, card.value)
        return self.cards

    def deal(self):
        x = random.choice(self.cards)
        print(x.suit, x.value)
        self.cards.remove(x)
        for card in self.cards:
            print(card.suit, card.value)

a = Deck()
a.shuffle()
a.deal()
