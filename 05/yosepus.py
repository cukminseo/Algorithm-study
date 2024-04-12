'''
Created by: minseo
Date: 4/10/24
Desc : https://www.acmicpc.net/problem/1158
Excute time : ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

queue = []
howmany = 41

# 2개보다 안되는 경우?
for who in range(1, howmany+1):
    queue.append(who)

# 두명 나올때 까지 죽이기
# while len(queue) > 2:
#     alive1 = queue.pop(0)
#     alive2 = queue.pop(0)
#     queue.pop(0)
#     queue.append(alive1)
#     queue.append(alive2)

# 머리쓰는 방법
while len(queue) > 2:
    queue.append(queue.pop(0))
    queue.append(queue.pop(0))
    queue.pop(0)

print(queue)

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
