import csv
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

search = input("검색어를 입력하세요...")

#url = f"https://section.blog.naver.com/Search/Blog.nhn?pageNo=1&orderBy=sim&keyword={quote_plus(search)}"

url = f'https://m.search.naver.com/search.naver?where=m_view&sm=mtb_jum&query={quote_plus(search)}'

html = urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

#total = soup.select('.name_blog')

total = soup.select('.api_txt_lines.total_tit')

searchList = []  # 2차원 구조

for i in total:
    temp = []  # a태그 하나의 정보
    temp.append(i.text)
    temp.append(i.attrs['href'])
    searchList.append(temp)
    print(i.attrs['href'])

f = open(f'{search}.csv', 'w', encoding='euc-kr', newline='')    

csvWriter = csv.writer(f)

for i in searchList:
    csvWriter.writerow(i)

f.close()   

print(f"{search}.csv 생성됨") 