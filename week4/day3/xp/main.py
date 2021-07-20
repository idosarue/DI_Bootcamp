# # 1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# zipped_dict = dict(zip(keys, values))
# print(zipped_dict)
#
# # 2
# # family = {"rick": 43, 'beth': 13, 'morty': 3, 'summer': 8}
# prices = []
# num_of_members = int(input('how many family members? '))
# names = []
# ages = []
# for num in range(1, num_of_members + 1):
#     name = input('what is your name? ')
#     age = int(input('what is your age? '))
#     names.append(name)
#     ages.append(age)
#
# new_family = {key:value for key, value in zip(names, ages)}
#
# for value in new_family.values():
#     if 3 <= value <= 12:
#         value = 10
#     elif value > 12:
#         value = 15
#     else:
#         value = 0
#     prices.append(value)
# total_price = sum(prices)
# print(new_family)
# print(f'the total is {total_price}')

# 3
brand_keys = ['name', 'creation_date', 'creator_name', 'type_of_clothes', 'international_competitors', 'number_stores', 'major_color']
brand_values = ["Zara", 1975, 'Amancio Ortega Gaona', ['men', 'women', 'children', 'home'], ['Gap', 'H&M', 'Benetton'], 7000, {'France' : 'blue', 'Spain ': 'red', 'US': ['pink', 'green']}]
brand = dict(zip(brand_keys, brand_values))
brand['number_stores'] = 2
print(f'Zara\'s costumers are : {str(brand["type_of_clothes"]).strip("[]")}')
brand["country_creation"] = "Spain"
if 'international_competitors' in brand.keys():
    brand['international_competitors'].append('Desigual')
del brand['creation_date']
print(brand['international_competitors'][-1])
print(brand['major_color']['US'])
print(len(brand))
print(brand.keys())
more_on_zara = {'creation_date': 1975, 'number_stores': 10000}
brand.update(more_on_zara)
print(brand['number_stores'])
# .update "updates" the key, value in the dict, so number of stores is updated to 10000

# 4
# 4.1
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
new_users = {}
for name in users:
    new_users[name] = users.index(name)
print(new_users)
users_dict = dict(zip(users, range(0, 5)))  # another way
print(users_dict)
new_users2 = {}

# 4.2

for name in users:
    new_users2[users.index(name)] = name
print(new_users2)
users_dict2 = dict(zip(range(0, 5), users))  # another way
print(users_dict2)

# 4.3
users_list = list(new_users)
users_list.sort()
new_users_dict = {}
for index, value in enumerate(users_list):
    new_users_dict[value] = index
print(new_users_dict)

new_users3 = {}

# 4.4
for name in users:
    if "i" in name:
        if name[0] == "M" or name[0] == "P":
            new_users3[name] = users.index(name)
print(new_users3)