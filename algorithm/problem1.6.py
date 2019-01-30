#문자열 압축 : 반복되는 문자의 개수를 세는 방식의 기본적인 문자열 압축 메서드를 작성하라. 
#예를 들어 문자열 aabccccaaa를 압축하면 a2b1c5a3이 된다.
#만약 압축된 문자열의 길이가 기존 문자열의 길이보다 길다면 기존 문자열을 반환해야 한다.
#문자열은 대소 알파벳(a~z)으로만 이루어져 있다.

inputstring = input("입력 : ")

c = inputstring[0]
zipcode = ""
ccount = 1
for i in range(1,len(inputstring)):
	if(inputstring[i]==c):
		ccount=ccount+1
	else:
		zipcode = zipcode+c+str(ccount)
		c = inputstring[i]
		ccount=1
zipcode = zipcode+c+str(ccount)

if(len(zipcode)>len(inputstring)):
	print(inputstring)
else:
	print(zipcode)
