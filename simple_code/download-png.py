#웹에 있는 데이터 다운로드하기
import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

#다운로드
mem = urllib.request.urlopen(url).read()

#파일로 저장하기
with open(savename, mode="wb") as f:
	f.write(mem)
	print("저장되었습니다.")