'''
Created by: minseo
Date: 4/3/24
Desc : 
Excute time : ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

import sys

sys.stdin = open('mapcodding.txt', 'r')
V, E = map(int, input().split())
graph_map = [[0 for _ in range(V+1)] for __ in range(V+1)]
for _ in range(E):
    start, stop = map(int, input().split())
    graph_map[start][stop] = 1
    graph_map[stop][start] = 1
print(graph_map)
# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
