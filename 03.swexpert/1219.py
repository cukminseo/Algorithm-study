'''
Created by: minseo
Date: 4/5/24
Desc : 
Excute time : 6.0230ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()
import sys
sys.stdin = open('SWEA1219.txt', 'r')


def DFS(here: int):
    visited[here] = True
    for next in range(100):
        if graph_map[here][next] and not visited[next]:
            DFS(next)


for cnt in range(1, 11):
    _, total_root = map(int, input().split())

    graph_map = [[0 for _ in range(100)] for __ in range(100)]
    visited = [False for _ in range(100)]

    # 노드 정보 기입
    node_info = list(map(int, input().split()))
    for i in range(0, total_root * 2, 2):
        graph_map[node_info[i]][node_info[i + 1]] = 1
        # 일방통행!!!!!!
        # graph_map[node_info[i + 1]][node_info[i]] = 1

    DFS(0)

    print(f"#{cnt}", end=" ")
    if visited[99]:
        print(1)
    else:
        print(0)

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
