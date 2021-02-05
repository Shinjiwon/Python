from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

baseUrl = 'https://www.google.com/search?q='
search = input("검색어를 입력하세요...")

url = baseUrl + quote_plus(search)

driver = webdriver.Chrome()
driver.get(url)


html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

rc = soup.select('.rc')
for i in rc:
    print(i.select_one('.LC20lb.DKV0Md').text)


# print(html)

driver.close()