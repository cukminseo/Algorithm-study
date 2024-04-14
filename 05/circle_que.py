'''
Created by: minseo
Date: 4/14/24
Desc :
교수님이 직접 만드신 좀비
교재 168페이지부터 공부하면서 구현하였습니다.
collections 활용하여 실제 Queue로 동작하도록 클래스 구현
Excute time : 84ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

import sys
from collections import deque
from typing import Any


class CircleQueue:
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
        self.que = deque([])

    def __len__(self) -> int:
        return self.no

    # Queue의 상태확인
    def is_empty(self) -> bool:
        return self.no <= 0

    def is_full(self) -> bool:
        return self.no >= self.capacity

    # 데이터 삽입
    def enqueue(self, x: Any) -> None:
        # 이미 가득 찼을 경우 예외처리 발생
        if self.is_full():
            raise CircleQueue.Full
        # rear에 값 추가
        self.que.append(x)
        # rear flag에 1을 추가
        self.rear += 1
        # 전체 데이터 갯수를 하나 추가
        self.no += 1
        # rear가 끝까지 오면 원형 Queue이므로 다시 0을 가리키도록 설계
        if self.rear == self.capacity:
            self.rear = 0

    def dequeue(self) -> Any:
        # 이미 비어 있을 경우 오류 발생
        if self.is_empty():
            raise CircleQueue.Empty
        x = self.que.popleft()
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x


sys.stdin = open("HW3.input.txt", "r")

Shalala, Zombie = map(int, input().split())
ability = list(map(int, input().split()))

queue = CircleQueue(2)



sys.stdin = open("HW3.jombie.txt")

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
