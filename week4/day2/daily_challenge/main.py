num = 6

num_of_i = 'i' * num
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
