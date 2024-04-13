'''
Created by: minseo
Date: 4/11/24
Desc : 백준 BFS, DFS 초보자 필수
Excute time : 0.0451000(time.perf_counter())
'''

import sys

from collections import deque

def DFS(node: int):
    dfs_visited[node] = True
    print(node, end = " ")
    for i in range(1, N+1):
        if graph[node][i] and not dfs_visited[i]:
            DFS(i)

def BFS():
    # 큐가 빌때까지 시행
    while bfs_queue:
        here = bfs_queue.popleft()
        bfs_visited[here] = True
        print(here, end = " ")
        for next in range(N+1):
            if graph[here][next] and not bfs_visited[next]:
                bfs_queue.append(next)
                bfs_visited[next] = True


sys.stdin = open('BAJ1260.txt', 'r')

N, M, V = map(int, input().split())

graph = [[False for _ in range(N+1)]for __ in range(N+1)]
# DFS 함수를 위한 방문 flag
dfs_visited = [False for _ in range(N+1)]
# BFS 함수를 위한 방문 flag
bfs_visited = [False for _ in range(N+1)]

bfs_queue = deque([])


for _ in range(M):
    N1, N2 = map(int, input().split())
    graph[N1][N2] = True
    graph[N2][N1] = True

DFS(V)
print()

bfs_queue.append(V)
BFS()