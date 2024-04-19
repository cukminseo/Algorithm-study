import sys
from collections import deque

sys.stdin = open("HW1.Miro.txt", "r")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def BFS(start):
    queue = deque([])
    queue.append(start)
    while queue:
        now_x, now_y = queue.popleft()
        miro[now_y][now_x] = 1
        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]
            if 0 <= next_x < 16 and 0 <= next_y < 16 and miro[next_y][next_x] != 1:
                if miro[next_y][next_x] == 3:
                    return 1
                queue.append((next_x, next_y))
    return 0


for i in range(1, 11):
    tc = int(input())

    miro = []

    for _ in range(16):
        miro.append(list(map(int, list(input()))))

    print(f"#{tc} {BFS((1, 1))}")
