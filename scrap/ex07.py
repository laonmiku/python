import requests
from bs4 import BeautifulSoup
import re
import csv

url="https://finance.naver.com/sise/sise_quant.naver"
res = requests.get(url)
# print(res.text)
soup = BeautifulSoup(res.text, 'lxml') 
# print(soup)
es = soup.find('table',attrs={'class':'type_2'}).find_all('tr')
print(len(es))

file = open('data/코스피거래상위1-100.csv','w',encoding='utf-8-sig', newline="") 
writer = csv.writer(file)
title = 'N	종목명	현재가	전일비	등락률	거래량	거래대금	매수호가	매도호가	시가총액	PER	ROE'.split('\t')
writer.writerow(title)
for e in es:
    columns = e.find_all("td")
    if len(columns) <= 1:
        continue
    # 둘다 동일한 결과나옴!
    # data = [col.get_text() for col in columns] 이거랑
    # data=[]
    # for col in columns:
    #     data.append(col.get_text()) 이거랑 같음 

    data=[]
    for col in columns:
        col = col.get_text()
        col = re.sub('\n|\t|상승|하락|보합','',col) #|=or 이거로 필터링걸어줌 그리고 re.sub 이거로 제외시킴
        data.append(col)
    #data = [re.sub('\n|\t|상승|하락|보합','',col.get_text()) for col in columns] 마찬가지로 위에꺼 이렇게 표현 가능
    writer.writerow(data)
    print (data)
