'''
Created by: minseo
Date: 4/10/24
Desc : 
Excute time : ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

Queue = []

for now in range(1, 4):
    Queue.append(now)

while Queue:
    print(Queue.pop(0))



# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
