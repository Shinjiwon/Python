from urllib.request import urlopen
# url 주소를 요청(request)하여, 응답(response)객체 생성
html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
print(html.read()) # 응답객체에서 존재하는 내용을 모두 읽어들임.