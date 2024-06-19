'''
Created by: minseo
Date: 3/19/24
Desc : sw아카데미 1206번 view 문제
Excute time : 1.1272500ms(time.perf_counter())
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
    for j in range(total_count - 4):
        # 주변 건물 최대 높이 확인
        on_window = building_list[j:j+4]
        good_view_cnt += max(on_window.pop(2)-max(on_window), 0)

    print(f"#{i+1} {good_view_cnt}")

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
