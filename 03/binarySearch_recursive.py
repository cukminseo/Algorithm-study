'''
Created by: minseo
Date: 3/27/24
Desc : 
Excute time : ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

def binarySearch(data, key, start = 0):
    end = len(data) - 1
    mid = (start + end) // 2
    if data[mid] == data:


data = [2, 4, 7, 9, 11, 19, 23]
key = 19
print(f"position : ")


# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
