'''
Created by: minseo
Date: 4/14/24
Desc :
교수님이 직접 만드신 좀비
Excute time : 0.1784ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

# import sys
from collections import deque


def BFS():
    # 거리(시간)측정
    distance = 0
    while myQueue:
        # 현위치 pop
        here = myQueue.popleft()
        for step in ability:
            myQueue.append(here+step)
        # 한번에 갈 수 있는 스텝을 다 갔을경우 1초를 증가
        distance += 1
        # zombie를 만났을 경우 break
        if zombie in myQueue:
            break
    return distance


# sys.stdin = open("HW3.jombie.txt", "r")

shalala, zombie = map(int, input().split())
ability = list(map(int, input().split()))

myQueue = deque([])

myQueue.append(shalala)
print(BFS())


# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
