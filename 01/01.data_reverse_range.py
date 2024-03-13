'''
주어진 범위 뒤집기
추천 문제 : 백준 10811 바구니 뒤집기
'''
data = [i for i in range(1, 7)]
howmany = len(data)

# 범위 지정
start = 3
end = 5

dummy = data[start:end + 1]
dummy.reverse()
data[start:end + 1] = dummy
print(data)
