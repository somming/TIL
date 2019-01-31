#행렬 회전 : 이미지를 표현하는 N*N 행렬이 있다. 
#이미지의 각 픽셀은 4바이트로 표현된다. 이 때, 이미지를 90도 회전시키는 메서드를 작성하라. 
#행렬을 추가로 사용하지 않고서도 할 수 있겠는가?

#90도 회전을 왼쪽으로? 오른쪽으로?
#행렬을 실제로 회전시켜보고 i,j 값을 비교해보며 규칙을 찾아낸다.

from random import *
import pandas as pd 

n = int(input("Enter the number of rows in a matrix : ")) 
a = [[0] * n for i in range(n)]
atr = [[0] * n for i in range(n)] #오른쪽으로 90도
atl = [[0] * n for i in range(n)] #왼쪽으로 90도  

col_names = [] 
row_names = [] 

for i in range (n): 
	col_names.append('col ' + str(i+1)) 
	row_names.append('row ' + str(i+1))
	for j in range(n): 
		a[i][j]=randint(1,100)

#오른쪽으로 회전

for i in range (n):
	for j in range(n):
		atr[i][j]=a[n-j-1][i]

#왼쪽으로 회전

for i in range (n):
	for j in range(n):
		atl[i][j]=a[j][n-i-1]

print(pd.DataFrame(a,columns = col_names, index = row_names)) 

print("\n오른쪽으로 90도")
print(pd.DataFrame(atr,columns = col_names, index = row_names)) 

print("\n왼쪽으로 90도")
print(pd.DataFrame(atl,columns = col_names, index = row_names)) 