'''
Created by: minseo
Date: 5/8/24
Desc : 
'''
import time


# 측정 시작
start_time = time.perf_counter()
a = 4
b=3
print(a,b)
a^=b
print(a,b)
b^=a
print(a,b)
a^=b
print(a,b)

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
