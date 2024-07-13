"""
Created by: minseo
Date: 2024-07-13
Desc : 
Excute time : 0.1018000ms(time.perf_counter())
Excute time : 68ms(BAJ)
"""

import time
import sys

# 측정 시작
start_time = time.perf_counter()
sys.stdin = open('4796.txt', 'r')

tc = 1
while True:
    L, P, V = map(int, input().split())

    # 0 0 0이 입력된 경우 중지
    if not L:
        break
    # 각 P일 마다 L일을 사용할 수 있는 첫 번째 케이스
    first_case = (V // P) * L
    # 마지막 남은 날짜 동안 혹은 L일 중 적은 날만큼 사용할 수 있는 두번째 케이스
    second_case = min(V % P, L)

    print(f"Case {tc}: {first_case + second_case}")
    tc += 1

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 시간: {(end_time - start_time) * 1000:.7f} milliseconds")
