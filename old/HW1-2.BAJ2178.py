'''
Created by: minseo
Date: 4/10/24
Desc : 
Excute time : ms(time.perf_counter())
'''
# import time

# 측정 시작
# start_time = time.perf_counter()

import sys
from collections import deque


def BFS(start_point):
    visited = [False for _ in range(computer + 1)]
    cnt = 0
    myQueue.append(start_point)
    while myQueue:
        now = myQueue.popleft()
        for next_step in range(1, computer + 1):
            if myGraph[now][next_step] and not visited[next_step]:
                visited[next_step] = True
                myQueue.append(next_step)
                cnt += 1
    return cnt


# sys.stdin = open("HW1-2.BAJ2178.txt", 'r')

computer, node = map(int, input().split())

myQueue = deque([])

myGraph = [[0 for _ in range(computer + 1)] for __ in range(computer + 1)]

start_depth = [-1] * (computer + 1)
for _ in range(node):
    end, start = map(int, input().split())
    myGraph[start][end] = True

for i in range(1, computer + 1):
    start_depth[i] = BFS(i)

for i in range(1, computer + 1):
    if start_depth[i] == max(start_depth):
        print(i, end=" ")

# 측정 종료 시간
# end_time = time.perf_counter()
# 실행 시간 출력
# print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
