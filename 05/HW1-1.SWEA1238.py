'''
Created by: minseo
Date: 4/11/24
Desc : 
Excute time : ms(time.perf_counter())
'''
import time
import sys
from collections import deque


# 측정 시작
start_time = time.perf_counter()

sys.stdin = open("SWEA1238.txt", "r")


def BFS():
    while queue:
        final = 0
        here = queue.popleft()
        visited[here] = True
        # print(here)
        for next in range(1, 101):
            if graph[here][next] and not visited[next]:
                final = max(final, next)
                queue.append(next)
                visited[next] = True
                distance[next] = distance[here] + 1
    return final




for tc in range(1, 11):
    lenth, start_point = map(int, input().split())
    info_list = list(map(int, input().split()))
    queue = deque([])

    graph = [[0 for _ in range(101)]for __ in range(101)]
    visited = [False] * 101
    parent = [False] * 101
    distance = [False] * 101

    for i in range(0, lenth, 2):
        start, end = info_list[i], info_list[i+1]
        graph[start][end] = True

    distance[start_point] = 1
    queue.append(start_point)
    BFS()

    max_dis = max(distance)

    # 가장 거리가 먼 값들의 리스트
    max_dis_index = []
    for index, value in enumerate(distance):
        # 최대거리 = 값인 친구들의 인덱스 구하기
        if value == max_dis:
            max_dis_index.append(index)

    print(f"#{tc} {max(max_dis_index)}")



# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
