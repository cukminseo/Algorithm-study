'''
Created by: minseo
Date: 3/28/24
Desc : 재귀 이용 선택정렬
Excute time : 0.0451000(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

import sys


def slect_sort_recursive(data:list, now:int = 0) -> list:
    """
    재귀적 방법을 이용한 선택정렬
    :param data: 숫자데이터타입의 리스트
    :param now: 현재 인덱스 위치
    :return:
    """
    if len(data) <= now:
        return data
    minimun_index=data[now:len(data)].index(min(data[now:len(data)]))+now
    data[now], data[minimun_index] = data[minimun_index], data[now]
    return slect_sort_recursive(data, now+1)


print(slect_sort_recursive([1,6,3,4,6,54,3245,324,3,45,456,4,5,4,2,3]))


# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 시간: {(end_time - start_time) * 1000:.7f} milliseconds")
