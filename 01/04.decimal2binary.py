'''
2진법 입력시 10진법으로 변환하는 코드
백준 추천문제 : 11005
'''

decimal = 30
remainder = decimal

while not(remainder == 1 or remainder == 0):
    each_point = remainder % 2
    remainder = remainder // 2
    result = str(each_point) + result

result += remainder

print(result)