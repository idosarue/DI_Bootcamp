
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2

    def area(self):
        return math.pi * self.radius**2

    def info(self, value):
        if value == 'radius':
            print('radius is:', self.radius)
        elif value == 'diameter':
            print('diameter is:', self.diameter)

    def __str__(self):
        return f'''
        your circle:
         {'*' * self.radius}
        *{" " * self.radius}*
        *{" " * self.radius}*
         {'*' * self.radius}
        '''

    def __add__(self, other_circle):
        if isinstance( other_circle, Circle):
            circle3 = Circle(self.radius + other_circle.radius)
            return  f'here is your new circle: {circle3}'
        else:
            return 'those are not 2 circles..'
    
    def __lt__(self, other):
        if self.radius < other.radius:
            return 'it\'s smaller'
        else:
            return 'it\'s not smaller'

    def __le__(self, other):
        if self.radius <= other.radius:
            return 'it\'s smaller or equal'
        else:
            return 'it\'s not smaller or equal'

    def __eq__(self, other):
        if self.radius == other.radius:
            return 'it\'s equal'
        else:
            return 'it\'s not equal'

    def __ne__(self, other):
        if self.radius != other.radius:
            return 'it\'s not equal'
        else:
            return 'it\'s equal'
    def __lt__(self, other):
        if self.radius < other.radius:
            return 'it\'s smaller'
        else:
            return 'it\'s not smaller'

    def __ge__(self, other):
        if self.radius >= other.radius:
            return 'it\'s bigger or equal'
        else:
            return 'it\'s not bigger or equal'

    def __gt__(self, other):
        if self.radius > other.radius:
            return 'it\'s bigger '
        else:
            return 'it\'s not bigger'
    li = []
    
    @classmethod
    def add_to_li(cls,a):
        cls.li.append(a.radius)
        return cls.li
circle1 = Circle(5)
circle2 = Circle(6)
circle1.info('radius')
circle1.info('diameter')
print(circle1)
print(circle1+circle2)
print(circle1 <= circle2)
print(circle1 < circle2)
print(circle1 > circle2)
print(circle1 == circle2)
print(circle1 != circle2)
print(circle1 >= circle2)
print(circle1.add_to_li(circle1))
print(circle2.add_to_li(circle2))
