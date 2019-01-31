#0행렬 : M*N 행렬의 한 원소가 0일 경우, 해당 원소가 속한 행과 열의 모든 원소를 0으로 설정하는 알고리즘을 작성하라.

#0~M 행 0~N 열 원소를 돌며 0인 장소의 위치를 기록해둔다.
#(m,n) 이 0이라면 (m,[0~N]) ([0~M],n)가 0이 되어야한다.

from random import *
import pandas as pd 

rnum = int(input("Enter the number of rows in a matrix : ")) 
cnum = int(input("Enter the number of cols in a matrix : ")) 
a = [[0] * cnum for i in range(rnum)]

zeropointx=[]
zeropointy=[]

for i in range(rnum):
	for j in range(cnum):
		a[i][j] = randint(0,10)
print(pd.DataFrame(a)) 

#0인 곳의 i,j 값 찾기
for i in range(rnum):
	for j in range(cnum):
		if(a[i][j]==0):
			zeropointx.append(i)
			zeropointy.append(j)

for i in range(len(zeropointx)):
	m = zeropointx[i]
	n = zeropointy[i]
	for j in range(rnum):
		a[j][n] = 0
	for j in range(cnum):
		a[m][j] = 0

print(pd.DataFrame(a)) 

