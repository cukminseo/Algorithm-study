"""
Created by: minseo
Date: 2024-07-13
Desc : 
Excute time : 0.0873000ms(time.perf_counter())
Excute time : 44ms(BAJ)
"""

import time
import sys

# 측정 시작
start_time = time.perf_counter()
sys.stdin = open('10162.txt', 'r')

# 시간 입력
A = 300
B = 60
C = 10

time_input = int(input())

a_freq = time_input // A
b_freq = time_input % A // B
c_freq = time_input % A % B // C

if a_freq*A+b_freq*B+c_freq*C == time_input:
    print(a_freq, b_freq, c_freq)
else:
    print(-1)


# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 시간: {(end_time - start_time) * 1000:.7f} milliseconds")
