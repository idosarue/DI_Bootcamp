import requests
from bs4 import BeautifulSoup
from requests.api import get
 
#**************** get data**************

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

# print(soup.body.contents)
# print(soup.find_all('div'))
# print(soup.find_all('a'))
# print(soup.find_all('title'))
# print(soup.find('a'))
# print(soup.find(id="score_28085632"))
# print(soup.select('.score')) # css selector
# print(soup.select('#score_28085632')) # css selector
links = soup.select('.storylink') # css selector
votes = soup.select('.score')
print(votes[0].get('id'))

#*******************project **********************

def create_custom_hn(links, votes):
    hn = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        # hn.append(title)
        # hn.append(href)
        if votes:
            points = int(votes[index].getText().replace(' points', ' '))
            hn.append(points)
            print(hn)
        else:
            print('non')
                
        hn.append({'title' : title, 'link' : href})
        
    return len(hn)

print(create_custom_hn(links,votes))
