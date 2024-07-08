"""
Created by: minseo
Date: 2024-07-08
Desc : 
Excute time : 0ms(time.perf_counter())
Excute time : 0ms(BAJ)
"""

import time
import sys

# 측정 시작
start_time = time.perf_counter()
sys.stdin = open('1302.txt', 'r')

N = int(input())
book_name_dict = {}
for _ in range(N):
    name = input()
    book_name_dict[name] = book_name_dict.get(name, 0) - 1

book_name_list = list(book_name_dict.items())

book_name_list.sort(key=lambda x: (x[1], x[0]))
print(book_name_list[0][0])

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 시간: {(end_time - start_time) * 1000:.7f} milliseconds")
