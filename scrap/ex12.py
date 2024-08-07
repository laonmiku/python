from selenium import webdriver
import time

options = webdriver.ChromeOptions() 
options.add_experimental_option('detach',True)
options.add_argument('headless') #브라우저 안열리게?안보이게하고 작업싴킴
options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36')
browser = webdriver.Chrome(options=options)
browser.maximize_window() 

query='레드벨벳 아이린 고화질'
url="https://www.google.com/search?q={}&sca_esv=0938baf10882972d&sca_upv=1&udm=2&biw=1277&bih=760&sxsrf=ADLYWIKf3Dkyk1aFXu5wlZbBGFbJo1Q_VQ%3A1722992086093&ei=1sWyZu-wBZqcvr0P98WEkAY&ved=0ahUKEwjv8_fZ1eGHAxUajq8BHfciAWIQ4dUDCBE&oq=%EA%B3%A0%ED%99%94%EC%A7%88+%EC%97%90%EC%8A%A4%ED%8C%8C%EC%9C%88%ED%84%B0&gs_lp=Egxnd3Mtd2l6LXNlcnAiGeqzoO2ZlOyniCDsl5DsiqTtjIzsnIjthLAyBBAjGCcyBhAAGAgYHkiSCFAAWABwAXgAkAEAmAEAoAEAqgEAuAEMyAEAmAIBoAIHmAMAiAYBkgcBMaAHAA&sclient=gws-wiz-serp".format(query)
browser.get(url)

prev_height = browser.execute_script('return document.body.scrollHeight')
# browser.execute_script('alert(arguments[0]),prev_height')
while True:
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(1)
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if prev_height == curr_height:
        print('스크롤완료')
        break
    prev_height = curr_height

from bs4 import BeautifulSoup
import re
soup = BeautifulSoup(browser.page_source,'lxml')


with open('data/image.html','w',encoding='utf-8') as file:
    file.write(soup.prettify())

es = soup.find_all('div',attrs={'class':re.compile('^eA0Zlc')})
for index,e in enumerate(es):
        title = e.find('div',attrs={'class':'juwGPd BwPElf OCzgxd'}).get_text()
        print(index+1,title)
print(len(es),'개')