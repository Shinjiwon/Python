from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys

# 함수 시작
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e: # 404에러 발생 예외처리 진행
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html, "html.parser")
        title = bsObj.body.h1
    except AttributeError as e: # 없는 속성을 사용했을 경우 예외처리가 진행됨.
        return None
    return title
# 함수 끝

title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
if title == None:
    print("발견 할 수 없다.")
else:
    print(title)