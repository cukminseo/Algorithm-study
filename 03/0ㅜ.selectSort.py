'''
Created by: minseo
Date: 3/27/24
Desc : 
Excute time : ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

def solve(Data, now):
    while now < howmany-1:
    where=Data.index(min(Data[now:howmany]))
    Data[now], Data[where] = Data[where], Data[now]

solve(0)
print(data)

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
