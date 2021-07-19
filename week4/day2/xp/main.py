


#  Exercise 1 : Favorite Numbers
# 1.1


my_fav_numbers = {10, 14, 7, 8, 9}
# 1.2
added_nums = [1, 2]
my_fav_numbers.update(added_nums)
print(my_fav_numbers)
# 1.3
my_fav_numbers.remove(14)
print(my_fav_numbers)
# 1.4
friend_fav_numbers = {1, 2, 3, 4, 5}
# 1.5
our_fav_numbers = set.union(my_fav_numbers, friend_fav_numbers)
print(our_fav_numbers)

# Exercise 2: Tuple
# 2.1
# you can't add more integers because tuples are immutable, however you can create a new tuple.
# example:
a_tuple = (1, 2, 3)
b_tuple = (3, 4, 5)
c_tuple = a_tuple + b_tuple
print(c_tuple)

# Exercise 3: Print A Range Of Numbers
# 3.1
for num in range(1, 21):
    print(num)

# Exercise 4: Floats
# 4.1
# Integers and floats are two different kinds of numerical data.
# An integer (more commonly called an int) is a number without a decimal point. A float is a floating-point number,
# which means it is a number that has a decimal place.
# 4.2
a, b, c, d = [1, 2, 3, 4]
print(a/1, b/1, c/1, d/1)
# 4.3
li = []
for num in range(1, 6):
    li.append(num)
    li[0] = 1.5
li.insert(2, 2.5)
li.insert(4, 3.5)
li.insert(6, 4.5)

print(li)

# 5
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# 5.1 / 5.2
for fruit in basket:
    if fruit == "Banana" or fruit == "Blueberries":
        basket.remove(fruit)
print(basket)

# 5.3
basket.append("kiwi")
print(basket)
# 5.4
basket.insert(0, "Apples")
print(basket)
# 5.5
print(basket.count("Apples"))
# 5.6
basket.clear()
# 5.7
print(basket)

# 7
my_name = "Ido"
counter = 0;
while True:
    user_name = input("Enter your name: ").lower().capitalize()
    if user_name == my_name:
        print("you have great name!")
        break
    else:
        counter += 1
        print("You should change your name..")
        if counter == 2:
            print("Ok I\'ll give you hint.. Enter MY name..")
        elif counter == 3:
            print('Whatever I quit')
            break
# 8

for num in range(1500, 2501):
    if num % 5 == 0 or num % 7 == 0:
        print(num)

# 9
user_fruit = input("Enter your favorite fruits separated by a space: ")
user_fruit_list = user_fruit.split(" ")
new_user_fruit = input("Enter a fruit: ")
if new_user_fruit in user_fruit_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")

# 10
my_toppings = ['mushrooms', 'olives', 'pineapple', 'onion', 'pepperoni']
list_of_toppings = []
while True:
    user_topping = input("choose topping for your pizza: ").lower()
    if user_topping in my_toppings:
        list_of_toppings.append(user_topping)
        print(f'okay we\'ll add {user_topping}')
        for topping in list_of_toppings:
            x = len(list_of_toppings) * 2.5
    elif user_topping == 'quit':
        if len(list_of_toppings) > 0:
            for topping in list_of_toppings:
                x = len(list_of_toppings) * 2.5
                print('your total is: ', x + 10)
                print('goodbye!')
                break
        else:
            print('your total is 10')
            print('goodbye!')
            break
    elif user_topping not in my_toppings:
        print('Sorry we don\'t have that..')

# 11

# 11 11.1-11.3
prices = []
num_of_members = input('how many family members? ')
counter = 0
while counter < int(num_of_members):
    counter += 1
    family_age = int(input("What is your age? "))
    if 12 > family_age > 3:
        prices.append(10)
    elif family_age > 12:
        prices.append(15)
print(sum(prices))

# 11. 4
num_of_people = int(input('how many people? '))
allowed_people = []
counter = 0
while counter < num_of_people:
    counter += 1
    person_name = input('What is your name? ')
    person_age = int(input(f'okay {person_name} how old are you? '))
    if person_age < 16 or person_age > 21:
        allowed_people.append(person_name)
print(allowed_people)

# 12

names_list = ['ido', 'john', 'doe']
age_list = []

for name in names_list:
    name_age = int(input(f'Hello {name} enter your age: '))
    print(names_list)
    if name_age > 16:
        age_list.append(name)
print(age_list)

# 13 / 14
sandwich_orders = ['cheese', 'blt', 'egg', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []
while sandwich_orders.count('pastrami') > 0:
    sandwich_orders.remove('pastrami')
for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
for finished in finished_sandwiches:
    print(f'made your {finished} sandwich')


