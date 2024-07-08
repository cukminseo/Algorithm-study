'''
Created by: minseo
Date: 3/20/24
Desc : 
Excute time : ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

data = [2, 4, 7, 9, 11, 19, 23]
key = 19

start = 0
end = len(data) - 1
while start <= end:
    mid = (start + end) // 2
    if data[mid] == key:
        print("find")
        break
    elif data[mid] > key:
        end = mid - 1
    else:
        start = mid + 1


# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
