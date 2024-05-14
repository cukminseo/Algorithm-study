import sys
from collections import deque


def BFS(task):
    while task:
        here = task.popleft()
        print(f"{here}", end=" ")
        for i in range(1, V+1):
            if graph_map[here][i]:
                pre_task[i] -= 1
                if pre_task[i] == 0:
                    task.append(i)

sys.stdin = open('SWEA1267.txt', 'r')

for tc in range(1, 11):
    print(f"#{tc}", end=" ")
    V, E = map(int, input().split())
    graph_map = [[0 for _ in range(1+V)] for __ in range(1+V)]
    pre_task = [0] * (V+1)

    now = deque([])


    # -1이 있는 위치는 이미 갔으므로 가지 않는다는 뜻, 여기서는 그냥 0번을 없앤 것
    pre_task[0] = -1

    edge_list = list(map(int, input().split()))
    for i in range(0, E*2, 2):
        start, end = edge_list[i], edge_list[i+1]
        graph_map[start][end] = 1
        pre_task[end] += 1

    for i in range(1, V+1):
        if pre_task[i] == 0:
            now.append(i)

    BFS(now)
    print()