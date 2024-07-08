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


def binary_search(query: int, data: list) -> int:
    """
    이분검색을 통한 리스트 검색
    :param query: 질의할 숫자
    :param data: 검색될 데이터
    :return: 1 or 0(int)
    """
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if query == data[mid]:
            return 1
        elif query > data[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0


sys.stdin = open('BAJ1920.txt', 'r')
# 데이터 갯수
data_len = int(input())
# 데이터 리스트(sort)
data_num_list = sorted(list(map(int, input().split())))
# 쿼리 갯수
query_len = int(input())
# 쿼리 리스트
query_num_list = list(map(int, input().split()))

for each_query in query_num_list:
    print(binary_search(each_query, data_num_list))

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 시간: {(end_time - start_time) * 1000:.7f} milliseconds")
