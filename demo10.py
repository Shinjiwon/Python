from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

# 제목형 tr 다음에 해당하는 형제 tr을 참조
for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)
