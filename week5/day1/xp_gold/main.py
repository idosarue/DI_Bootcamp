# 1

# Perimeter (P) = 2 · π · R
# area A=πr^2
import math
class Circle:
    def __init__(self, radius = 1.0):
        self.radius = radius

    def perimeter(self):
        p = 2 * math.pi * self.radius
        return p

    def area(self):
        a = math.pi * self.radius**2
        return a

    def defnition_of_circle(self):
        return 'A circle is a round shaped figure that has no corners or edges. '
    
circle1 = Circle(4)
print(circle1.defnition_of_circle())

# 2

import random

class MyList:
    def __init__(self, li):
        self.li = li

    def reverse(self):
        new_li = []
        while self.li:
            a = self.li.pop(-1)
            new_li.append(a)
        return new_li

    def sort(self):
        self.li.sort(key=lambda x:(not type(x) == str, x)) # items that are not strings will be at the and because True > false
        return self.li


    def create_list(self):
        li = [random.randint(a, 100) for a in range(len(self.li))]
        return li
b = MyList(['d',2,'a',1])
print(b.create_list())

# 3

class MenuManager:
    def __init__(self):
        self.menu = []

    def add_item(self, name, price, spice, gluten):
        my_dish = {'name': name, 'price': price, 'spice': spice, 'gluten' : gluten}
        self.menu.append(my_dish)
        return my_dish
    
    def update_item(self, name, price, spice, gluten):
        for item in self.menu:
            if item['name'] == name:
                item.update({'name' : name, 'price': price, 'spice': spice, 'gluten' : gluten})
                return item
    
    def remove_item(self, name):
        for item in self.menu:
            if item['name'] == name:
                self.menu.remove(item)

menu1 = MenuManager()
menu1.add_item('soup', 1, "b", True)
menu1.add_item('green', 1, "b", True)
menu1.update_item('green', 3, "b", True)
menu1.remove_item('green')

print(menu1.menu)
