'''
Created by: minseo
Date: 3/27/24
Desc : 
Excute time : ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

def binarySearch(data, key, start=0, end=None):
    if end is None:
        end = len(data) - 1
    if start > end:
        return -1
    mid = (start + end) // 2
    if data[mid] == key:
        return mid
    elif data[mid] > key:
        return binarySearch(data, key, start, mid-1)
    else:
        return binarySearch(data, key, mid+1, end)


data = [2, 4, 7, 9, 11, 19, 23]
key = 19
position = binarySearch(data, key)
if position == -1:
    print("탐색실패")
else:
    print(f"position : {position}")


# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
