from selenium import webdriver
from selenium.webdriver.common.by import By #특정 ID,class등을 찾아감 ID를 ㄱㅏ장 잘 찾음!
from selenium.webdriver.common.keys import Keys #키조작
import time

options = webdriver.ChromeOptions() #옵션을 설정하고 브라우저를 만들어야함!
options.add_experimental_option('detach',True) #마지막에 클로즈나 큐트안해주면 계속 살아있도록함.
browser = webdriver.Chrome(options=options)
browser.maximize_window() #전체화면

browser.get('https://www.naver.com/')
e = browser.find_element(By.ID, 'query')
e.send_keys('나도코딩')
time.sleep(2)
e.send_keys(Keys.ENTER)
time.sleep(3)

browser.close #browser.quit() 하면 브라우저 그룹 전체를 닫고 close는 그창 하나만 닫음