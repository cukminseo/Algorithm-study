"""
Created by: minseo
Date: 2024-07-11
Desc : 
Excute time : 0ms(time.perf_counter())
Excute time : 0ms(BAJ)
"""

import time
import sys

# 측정 시작
start_time = time.perf_counter()
sys.stdin = open('2548.txt', 'r')


# 입력
N = int(input())
num_arr = list(map(int, input().split()))

# 정렬하기
num_arr.sort()

# 중간값 찾기
mid_index = (N - 1) // 2
min_val = num_arr[mid_index]

print(min_val)


# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 시간: {(end_time - start_time) * 1000:.7f} milliseconds")
