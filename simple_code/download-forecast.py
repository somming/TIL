import urllib.request
import urllib.parse

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {
	'stnId':'108'
}
#사실 간단한 숫자인 경우에는 인코딩이 필요없지만, 한글일 경우 인코딩 필수!
params = urllib.parse.urlencode(values)
url = API+"?"+params
print("url=",url)

data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)