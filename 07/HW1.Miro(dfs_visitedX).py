import sys
from collections import deque

sys.stdin = open("HW1.Miro.txt", "r")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def DFS(next):
    now_x, now_y = next[0], next[1]
    for i in range(4):
        next_x = now_x + dx[i]
        next_y = now_y + dy[i]
        if 0 <= next_x < 16 and 0 <= next_y < 16 and miro[next_y][next_x] != 1:
            miro[next_y][next_x] = 1
            DFS((next_x, next_y))


for i in range(1, 11):
    tc = int(input())

    miro = []

    for _ in range(16):
        miro.append(list(map(int, list(input()))))

    DFS((1, 1))

    # 아직 3이 남아 있으면 못가본 것
    if max(map(max, miro)) == 3:
        print(f"#{tc} {0}")
    else:
        print(f"#{tc} {1}")
