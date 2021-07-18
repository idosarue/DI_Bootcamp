not_num = True
while not_num:
    user_num = input('enter a number between 1 and 100: ')
    if not user_num.isnumeric():
        print('not a number')
    user_num = int(user_num)
    if user_num not in range(1, 101):
        print('asd')
    else:
        not_num = False
        if user_num % 3 == 0 and user_num % 5 == 0:
            print('fizzbuz')
        elif user_num % 3 == 0:
            print('fizz')
        elif user_num % 5 == 0:
            print('buzz')