'''
2진법 입력시 10진법으로 변환하는 코드
백준 추천문제 : 11005
'''

decimal = 15
remainder = decimal
result = 0
cnt_iter = 0
while remainder != 0:
    each_point = remainder % 2
    remainder = remainder // 2
    result += each_point * (10**cnt_iter)
    cnt_iter += 1

print(result)