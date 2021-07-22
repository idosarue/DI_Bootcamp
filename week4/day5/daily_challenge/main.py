# Suppose the following input is supplied to the program:
# without, hello, bag, world
#
# Then, the output should be:
# bag,hello,without,world

sent = input('Enter a sequence of words separated by commas: ')
x = [char for char in sent if not char.isdigit()]
new_li = sorted("".join(x).split(','))
y = [word for word in new_li]
print(",".join(y))