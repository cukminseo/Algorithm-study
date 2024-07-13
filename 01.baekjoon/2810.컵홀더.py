"""
Created by: minseo
Date: 2024-07-13
Desc : 
Excute time : 0.083000ms(time.perf_counter())
Excute time : 36ms(BAJ)
"""

import time
import sys

# 측정 시작
start_time = time.perf_counter()
sys.stdin = open('2810.txt', 'r')

N = int(input())

seat = input()

couple = seat.count("LL")

if couple <= 1:
    print(N)
else:
    print(N + 1 - couple)

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 시간: {(end_time - start_time) * 1000:.7f} milliseconds")
