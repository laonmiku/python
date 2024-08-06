import requests
from bs4 import BeautifulSoup
import re #정규식쓰려면 필요함 re.compile('^search-product')

def create_soup(query,page):
    url="https://www.coupang.com/np/search?q={}&channel=auto&component=&eventCategory=SRP\
        &trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36\
        &filter=&isPriceRange=false&brand=&offerCondition=&rating=0&\
        page={}&rocketAll=false&searchIndexingToken=1=9&backgroundColor=".format(query,page)
    headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
            "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
        }
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text, 'lxml') 
    return soup

# soup = create_soup('노트북',3)
# es = soup.find_all("li",attrs={'class':re.compile('^search-product')}) #^search-product로 시작해서 꺽새^ 앞에 붙여줌
# print (len(es))

index = 0
items = []
for i in range(1,2):
    soup = create_soup('노트북',1)
    es = soup.find_all("li",attrs={'class':re.compile('^search-product')}) 
    for e in es:
        name = e.find('div',attrs={'class':'name'})
        if name:
            name = name.get_text().strip()
        else:
            continue
        price = e.find('strong',attrs={'class':'price-value'})
        if price:
            price = price.get_text().strip()
        else:
            continue
        image = e.find('img',attrs={'class':'search-product-wrap-img'})
        if image:
            image = 'https:'+ image['src'] #어트리부트?로 가져올려면 ['가져올거'] 적으면 댐
        else:
            continue
        index += 1
        print('번호:',index,' 이름:',name)
        print('가격:',price,'원')
        print('썸네일:',image)

        item = {'name':name, 'price':price, 'image':image}
        items.append(item)

        #이미지 다운로드
        # res_image = requests.get(image)
        # with open('images/img{}.jpg'.format(index),'wb') as file:
        #     file.write(res_image.content)

#items를 json파일로 저장 나중엔 임포트는 위로 올려서하기
import json
with open ('data/shop.json','w',encoding='utf-8') as file:
    file.write(json.dumps(items,indent=4, sort_keys=True, ensure_ascii=False)) # 들여쓰기, 소트는 모르겟고,아스키폴스해야한글로나옴

print('상품수 : ',index)