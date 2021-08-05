import psycopg2


HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'trumpisstupid15'
DATABASE = 'menu_manager'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )

cursor = connection.cursor()


# create table menu (item_name varchar(50) not null, price smallint not null, unique(item_name));




class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        save_q= f"insert into menu (item_name, price) values ('{self.name}', {self.price});"
        cursor.execute(save_q)
        connection.commit()
        print('item was added successfully.')

    def delete(self):
        del_q= f"delete from menu where item_name = '{self.name}';"
        cursor.execute(del_q)
        connection.commit()

    def update(self, name,price):
        update_q = f"update menu set item_name ='{name}', price = {price} where item_name = '{self.name}'"
        cursor.execute(update_q)
        connection.commit()

    @staticmethod
    def all():
        query = "select * from menu;"
        cursor.execute(query)
        results = cursor.fetchall()
        for item in results:
                print(item)
    
    @staticmethod
    def get_by_name(name):
        get_item_q = f"select item_name from menu where item_name = '{name}';"
        cursor.execute(get_item_q)
        result = cursor.fetchall()
        if result:
            for item in result:
                return item
        else:
            return None

