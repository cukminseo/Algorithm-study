'''
Created by: minseo
Date: 5/29/24
Desc : 실행 싯간: 0.0124160 milliseconds
'''
import time

# 측정 시작
start_time = time.perf_counter()

a = [1, 2, 3, 4, 5]

start = 0
end = len(a) - 1

while start < end:
    a[start], a[end] = a[end], a[start]
    start += 1
    end -= 1

print(a)
# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
