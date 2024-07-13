"""
Created by: minseo
Date: 2024-07-13
Desc : 
Excute time : 0.0769000ms(time.perf_counter())
Excute time : 0.32ms(BAJ)
"""

import time
import sys

# 측정 시작
start_time = time.perf_counter()
sys.stdin = open('5585.txt', 'r')

change = 1000 - int(input())

_500 = change // 500
_100 = change % 500 // 100
_50 = change % 500 % 100 // 50
_10 = change % 500 % 100 % 50 // 10
_5 = change % 500 % 100 % 50 % 10 // 5
_1 = change % 500 % 100 % 50 % 10 % 5 // 1

print(_500 + _100 + _50 + _10 + _5 + _1)

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 시간: {(end_time - start_time) * 1000:.7f} milliseconds")
