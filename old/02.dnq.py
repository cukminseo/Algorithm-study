'''
Created by: minseo
Date: 5/22/24
Desc : 
Excute time : ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

import sys

sys.stdin = open('02.dnq.txt', 'r')

a, b, c = map(int, input().split())


def get_some(b):
    if b == 1:
        return a % c
    halfpower = get_some(b // 2)
    if b & 1:
        return (halfpower ** 2 * a) % c
    else:
        return (halfpower ** 2) % c

print(get_some(b))

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
