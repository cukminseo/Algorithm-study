'''
Created by: minseo
Date: 5/8/24
Desc :
실행 싯간: 0.0148330 milliseconds
'''
import time

# 측정 시작
start_time = time.perf_counter()

data = [2, 3, 5, 4, 1]

for i in range(0, len(data)):
    for j in range(0, len(data) - i - 1):
        # print(i, j)
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

print(data)

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
