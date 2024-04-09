'''
Created by: minseo
Date: 4/9/24
Desc : 
Excute time : ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

import sys

pare = {'>': '<', ')': '(', ']': '[', '}': '{'}

sys.stdin = open('SWEA1218.txt', 'r')

for i in range(1, 11):

    #입력
    cnt = int(input())
    data = input()

    stack = []
    ans = 0
    isCorrect = True

    # while data:
    #     now = data.pop(0)
    for now in data:
        # 여는 괄호 라면
        if now in pare.values():
            stack.append(now)
        else:
            if not stack or stack[-1] != pare[now]:
                isCorrect = False
                break
            stack.pop()

    print(f"#{i}", end=" ")
    if not stack and isCorrect:
        print('1')
    else:
        print('0')


# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
