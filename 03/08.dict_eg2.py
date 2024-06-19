'''
Created by: minseo
Date: 3/20/24
Desc : 
'''
import time

# 측정 시작
start_time = time.perf_counter()

print()

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
