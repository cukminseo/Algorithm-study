'''
Created by: minseo
Date: 5/29/24
Desc : 실행 싯간: 0.0210000 milliseconds
'''
import time

# 측정 시작
start_time = time.perf_counter()

text = [3,1,4,1,5,1,2]
pattern = 151
howmany = len(str(pattern))

for i in range(len(text)-howmany+1):
    val = 0
    for now in range(i, i+howmany):
        val = val*10 + text[now]
    print(val)
    if val == pattern:
        print('find')

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
