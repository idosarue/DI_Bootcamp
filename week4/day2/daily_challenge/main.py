from datetime import datetime

today_date = input("Enter birth date in dd/mm/yyyy format:")
birth_date = datetime.strptime(today_date, '%d/%m/%Y')
age = "%d" % ((datetime.today() - birth_date).days/365)
num = int(age[-1])
if num > 0:
    num_of_i = 'i' * num
else:
    num_of_i = 'i' * 6
top_line = f'___{num_of_i}___'
space = " "
line_y = "|"
line_x = "_"
top_line_length = len(top_line)
happy = ' :H:a:p:p:y: '
num_of_spaces = (len(happy) - top_line_length) * space
birthday =" :B:i:r:t:h:d:a:y:"
birthday_length = len(birthday)
print(space,num_of_spaces, top_line)
print(space,line_y, happy, line_y)
print(line_x,line_y,line_x * len(happy),line_y,line_x)
print(line_y, " ^^^^^^^^^^^^^^^^^",line_y)
print(line_y, birthday, line_y)
print(line_y, space * birthday_length, line_y)
print("~~~~~~~~~~~~~~~~~~~~~~")
