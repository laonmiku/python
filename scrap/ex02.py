import requests
from bs4 import BeautifulSoup

#네이버증권 top종목
url= 'https://finance.naver.com/'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'lxml')

with open ('finace.html', 'w', encoding='utf-8') as file:
    file.write(res.text)

es = soup.find('tbody',attrs={'id': '_topItems1'}).find_all('tr', limit=5)
for e in es:
    title = e.find('a').get_text()
    td = e.find_all('td')
    price = td[0].get_text()
    updown = td[1].get_text()
    rate = td[2].get_text()
    print(title,price,updown, rate.strip())
