'''
Created by: minseo
Date: 4/3/24
Desc : 백준 9012번(제출시 조금 수정 필요)
Excute time : 0.0878750ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

import sys

sys.stdin = open('main.txt', 'r')
# num = int(input())
for tc in range(3):
    print(f"#{tc+1}", end=" ")
    stack = []
    pair = input()
    pair_len = len(pair)
    isCorrect = True
    for (now, each) in enumerate(pair):
        if each == '(':
            stack.append(each)
        else:
            if not stack or stack[-1] != '(':
                isCorrect = False
                break
            stack.pop()
    if not stack and isCorrect:
        print('YES')
    else:
        print('NO')

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
