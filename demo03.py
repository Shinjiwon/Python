from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
# bsObj 변수가 html응답객체를 통하여 DOM형태 parsing하여 참조
bsObj = BeautifulSoup(html, "html.parser")
print(bsObj.div)