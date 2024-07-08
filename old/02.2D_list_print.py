'''
Created by: minseo
Date: 3/20/24
Desc : 추천문제 SWEA 12712
Excute time : 0.0341670ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

data = [[1,2,3,4,5],
        [6,7,8,9],
        [10,11,12]]

for y in range(len(data)):
    for x in range(len(data[y])):
        print(data[y][x], end = '\t')
    print()

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"\n실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
