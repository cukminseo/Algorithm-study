'''
Created by: minseo
Date: 5/29/24
Desc : 
'''
import time

# 측정 시작
start_time = time.perf_counter()

import sys

sys.stdin = open("02.KMP.txt", "r")


def make_pi():
    PI[0] = -1
    i, j = 0, 1
    while j != (len(pattern) - 1):
        if pattern[i] == pattern[j]:
            PI[j + 1] = PI[j] + 1
            i += 1
            j += 1
        elif pattern[j] == pattern[0]:  # 0번째랑은 같음
            PI[j + 1] = 1
            i = 1
            j += 1
        else:  # 0번째와도 다름
            PI[j + 1] = 0
            i = 0
            j += 1


pattern = input()
PI = [0] * len(pattern)
make_pi()
print(PI)

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
