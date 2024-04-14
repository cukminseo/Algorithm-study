'''
Created by: minseo
Date: 4/14/24
Desc : 교수님이 직접 만드신 좀비
Excute time : 84ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

import sys
from collections import deque
from typing import Any


# 교재 168페이지부터 학습하여 활용
class FixedQueue:
    # 예외처리 클래스 선언
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int) -> None:
        """큐 초기화"""
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity

    def __len__(self) -> int:
        return self.no

    # Queue의 상태확인
    def is_empty(self) -> bool:
        return self.no < 0

    def is_full(self) -> bool:
        return self.no >= self.capacity

    # 데이터 삽입
    def enqueue(self, x: Any) -> None:
        # 이미 가득 찼을 경우 예외처리 발생
        if self.is_full():
            raise FixedQueue.Full

        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0


sys.stdin = open("HW3.jombie.txt")

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
