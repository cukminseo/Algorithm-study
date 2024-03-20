'''
Created by: minseo
Date: 3/20/24
Desc : 
Excute time : ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

data = [1, 2, 3, 4, 5, 6, 7]
key = 5

for i in range(len(data)):
    if key == data[i]:
        print(i + 1)

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
