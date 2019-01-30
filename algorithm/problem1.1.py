#중복이 없는가? 문자열이 주어졌을 때, 이 문자열에 같은 문자가 중복되어 등장하는지 확인하는 알고리즘을 작성하라. 

#나올수 있는 문자의 ASCII CODE를 생각한다.
#문자는 A~Z(65~90) a~z(97~122) 로 한정 대소문자 구분

import numpy as np 

scheck = np.zeros(58)
#scheck = [0 for i in range(58)]

inputstring = input("문자열을 입력하세요 : ")
slen=len(inputstring)

print(slen)

for i in range(slen):
	#print(inputstring[i])
	if(scheck[ord(inputstring[i])-65]==1):
			print("동일문자:"+inputstring[i])
			break;
	else:
		scheck[ord(inputstring[i])-65]=1
#print(scheck)