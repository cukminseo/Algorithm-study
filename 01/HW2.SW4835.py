'''
Created by: minseo
Date: 3/19/24
Desc : sw아카데미 구간합문제(4835)
Excute time : 0.0599160ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

import sys

sys.stdin = open('SW4835.txt', 'r')
test_case_count = int(input())
for test_case in range(1, test_case_count + 1):
    total_count, section_count = map(int, input().split())
    origin_list = list(map(int, input().split()))
    max_add = 0
    min_add = float("inf")
    for i in range(0, total_count - section_count+1):
        section_sum = sum(origin_list[i:i+section_count])
        if section_sum < min_add:
            min_add = section_sum
        if section_sum > max_add:
            max_add = section_sum
    result = max_add - min_add

    print(f"#{test_case} {result}")

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
