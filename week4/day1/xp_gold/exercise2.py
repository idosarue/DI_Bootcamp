user_month = int(input('enter a month num: '))
if user_month == 12 or user_month <= 2:
    print('winter')
elif user_month >= 9:
    print('autumn')
elif user_month >= 6:
    print('summer')
elif user_month >= 3:
    print('spring')
