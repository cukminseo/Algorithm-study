'''
Created by: minseo
Date: 3/13/24
Desc : str을 int로 변환
'''
data = ['1', '2', '3']

val = 0

for i in range(len(data)):
    val = val*10+int(data[i])

print(val)