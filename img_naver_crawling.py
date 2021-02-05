from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

# https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EA%BD%83
baseUrl = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
searchStr = input("검색어를 입력하세요.")
url = baseUrl + quote_plus(searchStr)
# url = baseUrl + searchStr 인코딩에러 발생

# html변수의 내용을 DOM기술 형태로 참조가 가능하도록 작업해주는 기능
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
img = soup.findAll(class_="_img")

# print(img[0])

n = 1 # 이미지파일명 일련번호 용도
for i in img:
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:
        with open("./img/" + searchStr + str(n) + ".jpg", "wb") as h:
            img = f.read()
            h.write(img)
    n += 1
    print(imgUrl)

print("다운완료")