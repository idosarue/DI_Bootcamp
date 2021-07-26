# 3

from main import Dog
from random import choice
class PetDog(Dog):
    def __init__(self,name,age, weight,  trained=False):
        super().__init__(name, age, weight)
        self.trained = trained
    
    def train(self):
        self.trained = True
        return f'{self.bark()} is trained {self.trained}'
    
    def play(self, *args):
        print(f'{self.name} {" ".join(args)} all play together')

    def do_a_trick(self):
        tricks_li = ['does a barrel roll','stands on his back legs','shakes your hand','plays dead']
        if self.trained == True:
            print(f'{self.name} {choice(tricks_li)}')
        else:
            print(f'Your dog {self.name} is not trained.. how do you expect him to do any tricks???')
            
dog1 = PetDog('hey', 5, 16)
dog2 = PetDog('lala', 3, 13)
dog3 = PetDog('blue', 5, 12)
print(dog1.train())
dog1.do_a_trick()
dog1.play(dog2.name,dog3.name)