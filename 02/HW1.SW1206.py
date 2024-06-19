'''
Created by: minseo
Date: 3/19/24
Desc : sw아카데미 1206번 view 문제
Excute time : 1.4775830ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

import sys

sys.stdin = open('SW1206.txt', 'r')

iter = 10
for i in range(iter):
    total_count = int(input())
    building_list = list(map(int, input().split()))
    good_view_cnt = 0
    for j in range(2, total_count - 2):
        # 주변 건물 최대 높이 확인
        left_view = max(building_list[j - 2:j])
        right_view = max(building_list[j+1:j+3])
        near_max_floor = max(left_view, right_view)
        # 조망권 확보시 확보 높이 확인
        if building_list[j] > near_max_floor:
            good_view_cnt += building_list[j] - near_max_floor
    print(f"#{i+1} {good_view_cnt}")

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
