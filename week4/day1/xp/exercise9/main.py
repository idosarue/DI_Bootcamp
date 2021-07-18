not_number = True
needed_height = 145
while not_number:
    user_height = input('Enter your height in inches as int: ')
    if not user_height.isnumeric():
        print('not a valid number try again')
    else:
        not_number = False
        user_height = int(user_height)
        user_height *= 2.54
        if user_height <= needed_height:
            print('Sorry you need to grow')
        else:
            print('you can ride')
