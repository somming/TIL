#문자열 회전 : 한 단어가 다른 문자열에 포함되어 있는지 판별하는 isSubstring이라는 메서드가 있다고 하자.
#s1,s2 두 문자열이 주어졌고, s2가 s1을 회전시킨 결과인지 판별하고자 한다. 
#'waterbottle'은 'erbottlewat'을 회전시켜 얻을 수 있는 문자열이다.
#isSubstring 메서드를 한 번만 호출해서 판별할 수 있는 코드를 작성하라.

#첫번째 문자열의 첫번째 문자를 두번째 문자열에서 찾는다.
#없으면 거기서 끝!
#n번째에 있다 하고 문자열의 길이가 m이라고 할 때, n부터 m까지의 뒤에다가 0부터 n-1까지 문자열을 붙힌다.  wat + erbottle
#isSubstring호출해서 true인지 판단.

#한 단어가 다른 문자열에 포함되어 있는지 판별하는 isSubstring함수

def isSubstring(s1,s2):
	if s1 in s2:
		print("true")
	else:
		print("false")
		
s1 = input("첫번째 문자열 입력 : ")
s2 = input("두번째 문자열 입력 : ")

start = s2.find(s1[0])

temp = s2[start:len(s2)] + s2[0:start]

isSubstring(s1,temp)


