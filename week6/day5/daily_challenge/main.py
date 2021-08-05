import requests
import random
import psycopg2

# SET client_encoding TO 'UTF8';

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'trumpisstupid15'
DATABASE = 'countries'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )

cursor = connection.cursor()



def get_random_data():
    response = requests.get("https://restcountries.eu/rest/v2/all")
    data = response.json()
    for _ in range(10):
        x = random.choice(data)
        save_q = f"insert into items (name, capital, flag, subregion, population) values(\'{x['name']}\', \'{x['capital']}\', \'{x['flag']}\', \'{x['subregion']}\', {x['population']});"
        cursor.execute(save_q)
        connection.commit()


get_random_data()
