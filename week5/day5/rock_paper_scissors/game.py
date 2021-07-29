import random
class Game:
    def __init__(self):
        pass

    def get_user_item(self):
        while True:
            user_choice = input('select (r)ock, (p)aper or (s)cissors: ')
            if user_choice == "r" or user_choice == "p" or user_choice == "s":
                return user_choice
            else:
                print('invalid input')

    def get_computer_item(self):
        cpu_choice = random.choice(["r", "p", "s"])     
        return cpu_choice

    def get_game_result(self, user_item, computer_item):
# rock crushes scissors, scissors cuts paper, but paper covers rock.
        if user_item == computer_item:
            return "draw"
        elif user_item == "s" and computer_item == "r":
            return "loss"
        elif user_item == "r" and computer_item == "s":
            return "win"
        elif user_item == "p" and computer_item == "s":
            return "loss"
        elif user_item == "s" and computer_item == "p":
            return "win"
        elif user_item == "r" and computer_item == "p":
            return "loss"
        elif user_item == "p" and computer_item == "r":
            return "win"        
    
    def play(self):
        self.user_item = self.get_user_item()
        self.cpu_item = self.get_computer_item()
        result = self.get_game_result(self.user_item, self.cpu_item)
        print(f'you chose : {self.user_item}, computer : {self.cpu_item}, result : {result}')
        return result


# a = Game()

