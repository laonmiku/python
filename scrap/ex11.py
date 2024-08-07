import requests
from bs4 import BeautifulSoup
import re

query='에스파 윈터'
url="https://www.google.com/search?q={}&sca_esv=0938baf10882972d&sca_upv=1&udm=2&biw=1277&bih=760&sxsrf=ADLYWIKf3Dkyk1aFXu5wlZbBGFbJo1Q_VQ%3A1722992086093&ei=1sWyZu-wBZqcvr0P98WEkAY&ved=0ahUKEwjv8_fZ1eGHAxUajq8BHfciAWIQ4dUDCBE&oq=%EA%B3%A0%ED%99%94%EC%A7%88+%EC%97%90%EC%8A%A4%ED%8C%8C%EC%9C%88%ED%84%B0&gs_lp=Egxnd3Mtd2l6LXNlcnAiGeqzoO2ZlOyniCDsl5DsiqTtjIzsnIjthLAyBBAjGCcyBhAAGAgYHkiSCFAAWABwAXgAkAEAmAEAoAEAqgEAuAEMyAEAmAIBoAIHmAMAiAYBkgcBMaAHAA&sclient=gws-wiz-serp".format(query)
headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
        }
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text, 'lxml') 

#print(res.text)
with open('data/image.html','w',encoding='utf-8') as file:
    file.write(soup.prettify())

es = soup.find_all('div',attrs={'class':re.compile('^eA0Zlc')})
for index,e in enumerate(es):
        title = e.find('div',attrs={'class':'juwGPd BwPElf OCzgxd'}).get_text()
        print(index+1,title)
print(len(es),'개')