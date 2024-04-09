'''
Created by: minseo
Date: 3/21/24
Desc : 백준 1920 수찾기
Excute time : 0.24350ms(time.perf_counter())
Excute time : 424ms(BAJ)
'''
import time

# 측정 시작
start_time = time.perf_counter()

import sys


def binary_search_recursive(query: int, data: list, start:int = 0, end:int = -1) -> int:
    """
    이분검색을 통한 리스트 검색
    :param query: 질의할 숫자
    :param data: 검색될 데이터
    :return: 1 or 0(int)
    """
    if end == -1:
        end = len(data)
    if start >= end:
        return 0
    mid = (start + end) // 2
    if query == data[mid]:
        return 1
    elif query > data[mid]:
        return binary_search_recursive(query, data, mid + 1, end)
    else:
        return binary_search_recursive(query, data, start, mid)



sys.stdin = open('03//BAJ1920.txt', 'r')
# 데이터 갯수
data_len = int(input())
# 데이터 리스트(sort)
data_num_list = sorted(list(map(int, input().split())))
# 쿼리 갯수
query_len = int(input())
# 쿼리 리스트
query_num_list = list(map(int, input().split()))

for each_query in query_num_list:
    print(binary_search_recursive(each_query, data_num_list))

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 시간: {(end_time - start_time) * 1000:.7f} milliseconds")
