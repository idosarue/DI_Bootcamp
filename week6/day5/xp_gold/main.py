# PART 1: Authentication CLI - Login:
import psycopg2
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'trumpisstupid15'
DATABASE = 'users'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )

# users_dict = {'ido' : '12345', 'john' : '12345678', 'jane' : '123456'}
# create table logged (username varchar(8), password bytea);


cursor = connection.cursor()

connection.commit()

while True:
    user_choice = input('choose exit\\login: ')
    if user_choice == 'exit' or user_choice == 'login':
        if user_choice == 'exit':
            break
        else:
            user_name = input('enter your user name: ')
            name_query = f"select username from logged where username = '{user_name}'"
            cursor.execute(name_query)
            name_result = cursor.fetchall()
            if name_result:
                user_password = input('enter your password: ')
                pw_query = f"select username from logged where password = '{user_password}'"
                cursor.execute(pw_query)
                pw_result = cursor.fetchall()
                if pw_result:
                    print('you are now logged in')
                    logged_in = [user_name, user_password]
                    break   
                else:
                    print('incorrect pw')
            else:
                print('invalid')
                to_log_in = input('would you like to sign up? y/n')
                if to_log_in == 'y' or to_log_in == 'n':
                    if to_log_in == 'y':
                        while True:
                            new_user_name = input('enter your new user name: ')
                            new_name_query = f"select username from logged where username = '{new_user_name}'"
                            cursor.execute(new_name_query)
                            new_name_result = cursor.fetchall()
                            if new_name_result:
                                print('username already exists')
                            else:
                                new_user_password = input('enter your new password: ')
                                s_query = f"insert into logged (username, password) values ('{new_user_name}', '{new_user_password}');"
                                cursor.execute(s_query)
                                connection.commit()
                                break
                    else:
                        break
                else:
                    print('invaild')
    else:
        print('invaild')

