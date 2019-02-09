from bs4 import BeautifulSoup
import urllib.request as request

#html 가져오기
url = "http://finance.naver.com/marketindex/"
res = request.urlopen(url)

#html 분석하기
soup = BeautifulSoup(res,"html.parser")

#원하는 데이터 추출하기
price = soup.select_one("div.head_info > span.value").string
print("usd/krw=",price)

'''다양한 추출방법
<html><body>
<h1>스크레핑</h1>
<p>웹 페이지를 분석하는 것<p/>
<p>원하는 부분을 추출하는 것</p>
</body></html>

h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling
'''


'''id로 요소 찾기
<html><body>
<h1 id="title">스크레핑</h1>
<p id="body">웹 페이지를 분석하는 것<p/>
<p>원하는 부분을 추출하는 것</p>
</body></html>

title = soup.find(id="title")
body = soup.find(id="body")
'''


'''다양한 추출방법
<html><body>
	<ul>
		<li><a href="http://www.naver.com">naver</a></li>
		<li><a href="http://daum.net">daum</a></li>
	</ul>
</body></html>

links = soup.find_all("a")

for a in links:
	href = a.attrs['href']
	text = a.string
	print(text,">",href)

'''

'''CSS선택자 사용하기
soup.select_one(<선택자>) 요소 하나를 추출
soup.select(<선택자>) 요소 여러개를 리스트로 추출
'''