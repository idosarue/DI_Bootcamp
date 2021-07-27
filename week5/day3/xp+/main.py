# 1
from datetime import MINYEAR, datetime
today = datetime.today()
print(today.strftime("%d/%m/%Y"))


# 2
def time_left():
    jan = "01/01/2022"
    dt = datetime.strptime(jan, "%d/%m/%Y")
    time = dt - today 
    return time

print(time_left())

# 3
def min_alive(birthdate):
    date = birthdate
    date = datetime.strptime(birthdate, '%d/%m/%Y')
    print(date)
    age = int(((datetime.today() - date).days/365))
    minutes = age * 525600
    print(f'you have been alive for {minutes} minutes')


min_alive("17/11/1997")

# 4
# Rosh Hashanah	6–8 Sep 2021*
def next_holiday():
    rosh_hashanah = "06/09/2021"
    dt = datetime.strptime(rosh_hashanah, "%d/%m/%Y")
    time = dt - today 
    return f"Rosh Hashanah is in {time} hrs"

print(next_holiday())

# 5
from decimal import Decimal
def age_on_jupiter(age_in_sec):
    earth_secs_in_year = 31557600
    age_on_earth = age_in_sec / earth_secs_in_year
    print(f'Your age on earth is {round(Decimal(age_on_earth),2)}') 
    mercury_secs_in_year = int(earth_secs_in_year * 0.2408467)
    age_on_mercury = age_in_sec / mercury_secs_in_year
    print(f'Your age on mecrucry is {round(Decimal(age_on_mercury),2)}') 
    venus_secs_in_year = int(earth_secs_in_year * 0.61519726)
    age_on_venus = age_in_sec / venus_secs_in_year
    print(f'Your age on venus is {round(Decimal(age_on_venus),2)}') 
    mars_secs_in_year = int(earth_secs_in_year * 1.8808158 )
    age_on_mars = age_in_sec / mars_secs_in_year
    print(f'Your age on mars is {round(Decimal(age_on_mars),2)}') 
    jupiter_secs_in_year = int(earth_secs_in_year *  29.447498 )
    age_on_jupiter = age_in_sec / jupiter_secs_in_year
    print(f'Your age on jupiter is {round(Decimal(age_on_jupiter),2)}') 
    uranus_secs_in_year = int(earth_secs_in_year * 84.016846)
    age_on_uranus = age_in_sec / uranus_secs_in_year
    print(f'Your age on uranus is {round(Decimal(age_on_uranus),2)}') 
    neptune_secs_in_year = int(earth_secs_in_year *  164.79132)
    age_on_neptune = age_in_sec / neptune_secs_in_year
    print(f'Your age on neptune is {round(Decimal(age_on_neptune),2)}') 


age_on_jupiter(1000000000)

# 6
from faker import Faker
import random
fake = Faker()
fake_names = []
fake_addresses = []
fake_codes = []
for i in range(10):
    fake_names.append(fake.name()) 
    fake_addresses.append(fake.address())
    fake_codes.append(fake.ean(length=8))

users = []


def new_users(**kwargs):
    users.append(kwargs)
    return users

new_users(name = random.choice(fake_names)  ,code = random.choice(fake_codes), address = random.choice(fake_addresses))
new_users(name = random.choice(fake_names)  ,code = random.choice(fake_codes), address = random.choice(fake_addresses))
print(new_users())