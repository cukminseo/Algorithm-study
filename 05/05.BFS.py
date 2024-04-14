'''
Created by: minseo
Date: 4/10/24
Desc : 
Excute time : ms(time.perf_counter())
'''
import time
from collections import deque

# 측정 시작
start_time = time.perf_counter()
import sys

sys.stdin = open('05.BFS.txt', 'r')

def BFS():
    while myQueue:
        here = myQueue.pop(0)
        visited[here] = True
        print(here)
        for next in range(howmany+1):
            if mygraph[here][next] and not visited[next]:
                myQueue.append(next)
                visited[next] = True
                Parent[next] = here
                Distance[next] = Distance[here] + 1


howmany, E = map(int, input().split())
myQueue = []
visited = [False for _ in range(howmany + 1)]
Parent = [0 for _ in range(howmany + 1)]
Distance = [0 for _ in range(howmany + 1)]

mygraph = [[0 for _ in range(howmany + 1)] for __ in range(howmany + 1)]
for _ in range(E):
    start, stop = map(int, input().split())
    mygraph[start][stop] = 1
    mygraph[stop][start] = 1

myQueue.append(1)
Parent[1] = -1
Distance[1] = 1
BFS()
print(Distance)
print(Parent)
# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
