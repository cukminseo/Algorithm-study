'''
Created by: minseo
Date: 5/29/24
Desc : 
'''
import time

# 측정 시작
start_time = time.perf_counter()

str = 'this is sample string'
c1 = str.find('i')
c2 = str.find('i', 10)
c3 = str.find('i', 0, 10)

print(c1)
print(c2)
print(c3)

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
