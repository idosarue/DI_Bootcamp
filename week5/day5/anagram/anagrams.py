
from anagram_checker import AnagramChecker

def menu():
    a = AnagramChecker()
    while True:
        user_choice = input('''
        (a) play
        (b) exit
        ''')

        if user_choice == 'b':
            print('ok goodbye')
            break
        elif user_choice == 'a':
            while True:
                user_word = input('enter a  word: ')
                if len(user_word.split()) > 1:
                    print('please enter one word')
                else:
                    if a.is_valid_word(user_word):
                        if user_word.isalpha():
                            user_word.strip()
                            print(f'your word: {user_word.upper()}')
                            return f' anagrams for your word: {",".join(a.get_anagrams(user_word))}.'
                        else:
                            print('invalid input')
                    else:
                        print('invalid word')
        else:
            print('command not recognized')
print(menu())

