'''
Created by: minseo
Date: 5/22/24
Desc : 
Excute time : ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()
data = [3, 2, 4, 6, 9, 1, 8, 7, 5]


def quick_sort(_from, _to):
    if _from < _to:
        pivot = partition(_from, _to)
        quick_sort(_from, pivot - 1)
        quick_sort(pivot + 1, _to)


def partition(left, right):
    where = left
    pivot = data[where]
    while left < right:
        while left < len(data) and data[left] <= pivot:
            left += 1
        while data[right] > pivot:
            right -= 1
        if left < right:
            data[left], data[right] = data[right], data[left]
    data[where], data[right] = data[right], data[where]

    return right

quick_sort(0, len(data)-1)
print(data)

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
