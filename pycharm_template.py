"""
Created by: minseo
Date: ${DATE}
Desc : 
Excute time : 0ms(time.perf_counter())
Excute time : 0ms(BAJ)
"""

import time
import sys

# 측정 시작
start_time = time.perf_counter()
sys.stdin = open('input.txt', 'r')






# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 시간: {(end_time - start_time) * 1000:.7f} milliseconds")