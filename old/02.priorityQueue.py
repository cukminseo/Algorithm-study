'''
Created by: minseo
Date: 6/5/24
Desc : 
'''
import time

# 측정 시작
start_time = time.perf_counter()

import heapq

q = []

heapq.heappush(q, 3)
heapq.heappush(q, 10)
heapq.heappush(q, 1)
heapq.heappush(q, 0)
heapq.heappush(q, 4)

print(q)  # [0, 1, 3, 10, 4]

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
