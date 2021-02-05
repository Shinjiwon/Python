from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

# 현재 이미지 위치에서 위의 가격을 참조하는 구문. get_text()사용할려면 previous_sibling 같이 단수로 써야함.
print(bsObj.find("img",{"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())