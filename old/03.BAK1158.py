'''
Created by: minseo
Date: 4/10/24
Desc : 
Excute time : ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

from collections import deque


people, times = map(int, input().split())
queue = deque(range(1, people+1))

print("<", end="")
while len(queue) > 1:
    for _ in range(times-1):
        queue.append(queue.popleft())
    print(f"{queue.popleft()}", end=", ")

print(f"{queue.popleft()}", end="")
print(">")


# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
