'''
주어진 범위만 뒤집기

추천 문제 : 백준 10811 바구니 뒤집기
'''

data = [i for i in range(1, 7)]

# 범위 지정
start = 3
end = 5

dummy = data[start:end + 1]
dummy.reverse()

#바꾼 값으로 수정
data[start:end + 1] = dummy

print(data)
