#회문 순열 : 주어진 문자열이 회문의 순열인지 아닌지 확인하는 함수를 작성하라. 회문이란 앞으로 읽으나 뒤로 읽으나 같은 단어 혹은 구절을 의미하며, 
#순열이란 문자열을 재배치하는 것을 뜻한다.

#회문이 되려면?
'''
	0.공백을 제거하고
	1.입력이 홀수 개라면, 한개 문자만 홀수개. 나머지 문자는 짝수개가 필요하다. 
	2.입력이 짝수 개라면, 문자들이 전부 짝수 개여야 한다. 
'''
import numpy as np 

scheck = np.zeros(128)

oddnum=False;#홀수개인 문자 등장
permutation=True


#공백 제거 및 대소문자 맞추기

inputstring = input("입력 : ")
inputstring = inputstring.replace(" ", "")
inputstring = inputstring.lower()
#print(inputstring)
for i in range(len(inputstring)):
	scheck[ord(inputstring[i])]+=1

#print(scheck)
if (len(inputstring)%2==1) :
	for i in range(128):	
		if(scheck[i]%2==1):#홀수개인 문자
			if(oddnum):
				#print("oddnum double exist"+chr(i))
				permutation=False;
				break;
			else:
				oddnum=True
				#print("oddnum exist"+chr(i))


else:
	for i in range(128):	
		if(scheck[i]%2==1):#홀수개인 문자
			permutation=False;
			break;


if(permutation):
	print("회문의 순열입니다.")
else:
	print("회문의 순열이 아닙니다.")