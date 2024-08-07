from selenium import webdriver
from selenium.webdriver.common.by import By #특정 ID,class등을 찾아감 ID를 ㄱㅏ장 잘 찾음!
from selenium.webdriver.common.keys import Keys #키조작
import time
import re
from selenium.webdriver.support.ui import WebDriverWait #최대로 기다리는걸 지정해줌
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions() 
options.add_experimental_option('detach',True) 
browser = webdriver.Chrome(options=options)
browser.maximize_window() 

def wait_until(xpath):
    WebDriverWait(browser, 120).until(EC.presence_of_all_elements_located((By.XPATH, xpath))) 

browser.get('https://flight.naver.com/')
#e = browser.find_element(By.XPATH,'////*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]') 문서전체에서 찾음
e = browser.find_element(By.XPATH,'//button[text()="가는 날"]') #버튼에 텍스트값까지해서 찾음!
e.click()

#가는 날 클릭
xpath = '//b[text()="28"]'
wait_until(xpath)
es = browser.find_elements(By.XPATH,xpath) #모든 28일중에 이번달이니까첫번쨰! 그래서 배열중에 [0]번쨰
es[0].click()
#오는 날 클릭
xpath = '//b[text()="30"]'
wait_until(xpath)
es = browser.find_elements(By.XPATH,xpath)
es[0].click()

#도착 클릭
xpath='//b[text()="도착"]'
wait_until(xpath)
e = browser.find_element(By.XPATH, xpath)
e.click()
#도착지 클릭(국내)
xpath='//button[text()="일본"]'
wait_until(xpath)
e = browser.find_element(By.XPATH, xpath)
e.click()
#도착지 클릭(제주)
xpath='//i[contains(text(),"TYO")]'
wait_until(xpath)
e = browser.find_element(By.XPATH, xpath)
e.click()

#검색버튼 클릭
xpath='//span[contains(text(),"검색")]'
wait_until(xpath)
e = browser.find_element(By.XPATH, xpath)
e.click()

#-------------------------항공권선택(가장상단)
first = '//*[@id="container"]/div[5]/div/div[3]/div[1]'
wait_until(first)
e = browser.find_element(By.XPATH, first)
print(e.text)

#------------------------항공권선택 전부출력  
es = browser.find_elements(By.XPATH, '//*[contains(@class,"concurrent_ConcurrentItemContainer__NDJda")]')
es = es[:10]
for e in es:
  print(e.text)
  print('-' * 50)
print("전체검색수:", len(es))

browser.close
