import requests
import time
def time_to_load(url):
    response = requests.get(url)
    if response:
        start = time.time()
        requests.get(url)
        end = time.time()
        print(f'{url} took {end-start} secs to load')
    else:
        print('An error has occurred.')

time_to_load('https://www.google.co.il/')
time_to_load('https://www.ynet.co.il/home/0,7340,L-8,00.html')