import random

user_string = input('enter a string with 10 character: ')
if len(user_string) < 10:
    print('too short')
elif len(user_string) > 10:
    print('too long')
else:
    li = []
    li2 = []
    print((user_string[0], user_string[-1]))
    for i in user_string:
        li.append(i)

        li2.append(i)
        x = str(li).strip("[]")
        x = "".join(li)
        print(x)
        random.shuffle(li2)
        y = str(li2).strip("[]")
        y = "".join(li2)
        print(li2)

