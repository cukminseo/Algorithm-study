"""
Created by: minseo
Date: 2024-07-13
Desc : 
Excute time : 0.1292000 milliseconds(time.perf_counter())
Excute time : 60ms(BAJ)
"""

import time
import sys

# 측정 시작
start_time = time.perf_counter()
sys.stdin = open('2720.txt', 'r')

tc = int(input())
for _ in range(tc):
    # 단위
    quarter = 25
    dime = 10
    nickel = 5
    penny = 1

    # 거스름돈 입력
    change = int(input())

    # 잔돈 계산
    q = change // quarter
    d = change % quarter // dime
    n = change % quarter % dime // nickel
    p = change % quarter % dime % nickel // penny

    # 출력
    print(q, d, n, p)



# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 시간: {(end_time - start_time) * 1000:.7f} milliseconds")
