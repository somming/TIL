#하나 빼기 : 문자열을 편집하는 방법에는 세 가지 종류가 있다. 문자 삽입, 문자 삭제, 문자 교체.
#문자열 두 개가 주어졌을 때, 문자열을 같게 만들기 위한 편집 횟수가 1회 이내인지 확인하는 함수를 작성하라.

#문자열 길이차이가 1이상 나면 out!
#문자열 길이차이가 1이라면, 긴 쪽에서 삭제 또는 짧은 쪽에서 삽입이 일어나야 한다.
#문자열 길이가 같다면 교체가 일어나야 한다.

inputA = input("문자열A 입력하세요 : ")
inputB = input("문자열B 입력하세요 : ")

inputAlen = len(inputA)
inputBlen = len(inputB)

isedit = False #편집을 이미 했는지!
editcheck = True

j=0 #inputB의 index

if(abs(inputAlen-inputBlen)>1):
	print(False)
else:
	if(inputAlen>inputBlen):
		#A에서 삭제가 일어나야 한다.(또는 B에서 삽입이 일어나야 한다.)
		for i in range(inputAlen):
			#print(inputA[i],inputB[j])
			if(inputA[i]==inputB[j]):#문자가 같다면 넘어가기
				j+=1
				continue
			else:# 문자가 다르다면!
			# 편집이 일어났는지 확인. 안일어났으면 A에서 해당 문자 삭제하고 뒤부터 계속 비교. 뒤에서 또 다른 부분이 나오면 out!
				if(isedit):
					editcheck = False
					break
				else:
					isedit = True #삭제됐다고 가정하고! j는 증가시키지 않는다.
					#print(inputA[i]+"삭제!")
					continue

	elif(inputAlen<inputBlen):
		#A에서 삽입이 일어나야 한다. (또는 B에서 삭제가 일어나야 한다.)
		for i in range(inputBlen):
			#print(inputA[i],inputB[j])
			if(inputA[j]==inputB[i]):#문자가 같다면 넘어가기
				j+=1
				continue
			else:# 문자가 다르다면!
			# 편집이 일어났는지 확인. 안일어났으면 B에서 해당 문자 삭제하고 뒤부터 계속 비교. 뒤에서 또 다른 부분이 나오면 out!
				if(isedit):
					editcheck = False
					break
				else:
					isedit = True #삭제됐다고 가정하고! j는 증가시키지 않는다.
					#print(inputB[i]+"삭제!")
					continue
	else:
		#A나 B에서 교체가 일어나야 한다.
		for i in range(inputBlen):
			#print(inputA[i],inputB[j])
			if(inputA[i]==inputB[i]):#문자가 같다면 넘어가기
				continue
			else:# 문자가 다르다면!
			# 편집이 일어났는지 확인. 안일어났으면 교체처리하고 뒤부터 계속 비교. 뒤에서 또 다른 부분이 나오면 out!
				if(isedit):
					editcheck = False
					break
				else:
					isedit = True #교체 처리
					#print(inputB[i]+"삭제!")
					continue
if(editcheck):
	print("true")
else:
	print("false")