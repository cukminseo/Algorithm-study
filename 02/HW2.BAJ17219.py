'''
Created by: minseo
Date: 3/24/24
Desc : 백준 17219번 비밀번호 찾기(딕셔너리 응용)
Excute time : 12380ms(BAJ)
'''
import time

# 측정 시작
start_time = time.perf_counter()

import sys

sys.stdin = open('BAJ17219.txt', 'r')
# 데이터 갯수

database = {}
save_num, query_num = map(int, input().split())
for _ in range(save_num):
    site, pw = input().split()
    database[site] = pw
for _ in range(query_num):
    query_site = input()
    print(database[query_site])


# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 시간: {(end_time - start_time) * 1000:.7f} milliseconds")
