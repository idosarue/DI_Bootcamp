from main import MenuItem


def load_manager(name, price):
    a = MenuItem(name, price)
    return a

def show_user_menu():
    print('MENU')
    user_choice = input('''
    (a) Add an item
    (d) Delete an Item
    (v) View the menu
    (x) Exit
    ''')
    return user_choice

def add_item_to_menu(name, price):
    load_manager(name, price).save()
    

def remove_item_from_menu(name, price = None):
    if load_manager(name, price).get_by_name(name):
        load_manager(name,price).delete()
        print('removed item')
    else:
        print('eror')

def show_restaurant_menu(name= None, price = None):
    load_manager(name, price).all()

def run():
    while True:
        user_choice = show_user_menu()
        if user_choice == "a" or user_choice == "d" or user_choice == "v" or user_choice == "x":
            if user_choice == "a":
                item = input('choose item name:')
                if not item.isdigit():
                    item_price = input('choose item price:')
                    add_item_to_menu(item, item_price)
                else:
                    print('invalid type')
            elif user_choice == "d":
                item = input('choose item name:')
                remove_item_from_menu(item)
            elif user_choice == "v":
                show_restaurant_menu()
            else:
                print('goodbye!')
                show_restaurant_menu()
                break
        else:
            print('invalid input')



run()
    