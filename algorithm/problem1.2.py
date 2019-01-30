#순열 확인 : 문자열 두 개가 주어졌을 때 이 둘이 서로 순열관계에 있는지 확인하는 메서드를 작성하라

#먼저 문자열의 두 개의 길이가 다르면 X
#각각의 문자열을 A,B라고 했을 때, A에 있는 문자의 종류와 각 갯수가 B에 있는 문자의 종류와 각 갯수가 맞아야 한다.

import numpy as np 

#문자 갯수를 체크하는 배열
scheck1 = np.zeros(58)
scheck2 = np.zeros(58)

permutation=True;

#문자열 두개 입력받기
inputA = input("문자열 A : ")
inputB = input("문자열 B : ")

if(len(inputA)!=len(inputB)):
	print("false")
else:
	for i in range(len(inputA)):
		scheck1[ord(inputA[i])-65]=scheck1[ord(inputA[i])-65]+1
	for i in range(len(inputB)):
		scheck2[ord(inputB[i])-65]=scheck2[ord(inputB[i])-65]+1

	for i in range(58):	
		if(scheck1[i]!=scheck2[i]):
			permutation=False
			break
	if(permutation):
		print("순열관계입니다.")
	else:
		print("순열관계가 아닙니다.")