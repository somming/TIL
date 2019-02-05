#중복이 없는가? 문자열이 주어졌을 때, 이 문자열에 같은 문자가 중복되어 등장하는지 확인하는 알고리즘을 작성하라. 

#나올수 있는 문자의 ASCII CODE를 생각한다.

import numpy as np 

scheck = np.zeros(128)
#scheck = [0 for i in range(58)]

inputstring = input("문자열을 입력하세요 : ")
slen=len(inputstring)

print(slen)

for i in range(slen):
	#print(inputstring[i])
	if(scheck[ord(inputstring[i])]==1):
			print("동일문자:"+inputstring[i])
			break;
	else:
		scheck[ord(inputstring[i])]=1
#print(scheck)


'''모범답안
import unittest # 단위 테스트 프레임워크

#단위 테스트란? 모듈 또는 응용 프로그램 내의 개별 코드 단위가 예상대로 작동하는지 확인하는 반복 가능한 활동
#unittest : Python에 포함된 다양한 테스트를 자동화할 수 있는 기능이 포함되어 있는 표준 라이브러리

#unittest모듈 사용
#예제 코드 작성
#TestCase를 작성하기 위해 unittest.TestCase를 상속한 테스트 클래스 작성
#test_ 로 시작하는 메소드는 모두 테스트 메소드가 된다.
#test_unique() 메소드는 단순 실행 여부만 판별
#unittest.main() 코드를 통해 테스트가 수행된다.

#setUp() : Fixture 입니다. 테스트 전에 수행됩니다.
#tearDown() : Fixture입니다. 테스트 후에 수행됩니다.
#self.assertTrue(x) bool(x) is True
#self.assertFlase(x) bool(x) is False
#self.assertEqual(custom_function(self.file_name), 3) 구문은 custom_function(file_name) 을 수행하고 결과가 3이면 테스트를 통과합니다.

def unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True


class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
'''