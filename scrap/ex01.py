import requests
from bs4 import BeautifulSoup

url= 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
res = requests.get(url)

#requests쓰깅
# print(res.text)
# with open('cvg.html', 'w', encoding='utf-8') as file:
#     file.write(res.text)

#BeautifulSoup쓰깅
soup = BeautifulSoup(res.text, 'lxml')
# title = soup.title
# print(title.get_text())
movie = soup.find('div',attrs={'class':'sect-movie-chart'})
movies = movie.find_all('li')
#print(len(movies))

for index,m  in enumerate(movies):
    title = m.find('strong',attrs={'class':'title'}).get_text()
    img = m.find('img').attrs['src']
    link = m.find('a',attrs={'class':'link-reservation'})['href']
    date = m.find('span',attrs={'class', 'txt-info'}).find('strong').get_text().lstrip()
    percent = m.find('strong', attrs={'class':'percent'}).find('span').get_text()
    print (str(index+1),title)
    print(img)
    print('개봉일',date[0:10])
    print('예매율',percent)
    print('http://www.cgv.co.kr' + link)
    print('-'*80)


