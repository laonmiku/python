from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions() 
options.add_experimental_option('detach',True)
options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36')
browser = webdriver.Chrome(options=options)
browser.maximize_window() 

url="https://land.naver.com/"
browser.get(url)

e = browser.find_element(By.ID,"queryInputHeader")
e.send_keys('서구')
e.send_keys(Keys.ENTER)

from bs4 import BeautifulSoup
soup = BeautifulSoup(browser.page_source,'lxml')

es = soup.find_all('div',attrs={'class':('item')})
for index,e in enumerate(es):
        title = e.find('div',attrs={'class':'title'}).get_text()
        address = e.find('div',attrs={'class':'address'})
        if address:
            address = address.get_text()
        else:
            address = ""    
        info = e.find('div',attrs={'class':'info_area'})
        if info:
            info=info.get_text()
        else:
            info=""
        print(index+1)
        print(title,'||',address,'||',info)
print('total : ',len(es),'개')