import requests
from bs4 import BeautifulSoup
import re

index = 0
#쿠팡에서 노트북 검색>1페이지데이터>맨처음엔 디폴트값이라 2페이지 갓다가 다시 1페이지와야 찍힘
#이 모든작업을 6번 반복하게만들어줌!for i in range(1,6):
#페이지가 변수니까 page={} 이렇게 해주고 맨뒤에 .format(i)를 해주면 {}여기에 i가 들어감
for i in range(1,6):
    url= 'https://www.coupang.com/np/search?q=노트북&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor='.format(i)
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
    }
    res = requests.get(url,headers=headers)

    soup = BeautifulSoup(res.text, 'lxml') 

    es = soup.find_all("li",attrs={'class':re.compile('^search-product')})
    #print(len(es))

    
    for e in es:
        name = e.find('div', attrs={'class':'name'}).get_text().strip()
        price = e.find('strong',attrs={'class':'price-value'}).get_text()
        #'Apple'이 들어간 네임은 제외하고 나오게함 continue 아예 스킵
        if 'Apple' in name:
            continue
        count = e.find('span', attrs={'class':'rating-total-count'})
        if count :
            count = count.get_text()
        else :
            continue
        #[1:-1] 이러면 0번째와 마지막번쨰뺴고 가져온다는말 마지막에서 한개 앞  
        count = int(count[1:-1])
        if count < 200:
            continue
        rating = e.find('em',attrs={'class':'rating'})
        if rating :
            rating = rating.get_text()
        else :
            continue
        rating = float(rating)
        if rating < 5.0:
            continue
        index += 1
        print('[',index,']')
        print('제목',name)
        print('가격:', price,'원')
        print('평점:', count,'건',rating,'점')
        print('-'*50)