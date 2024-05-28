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

print()


def quck_python(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    less, equal, bigger = [], [], []
    for each in range(len(data)):
        each = data.pop()
        if each < pivot:
            less.append(each)
        elif each > pivot:
            bigger.append(each)
        else:
            equal.append(each)

    return quck_python(less)+equal+quck_python(bigger)


print(quck_python(data))

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
