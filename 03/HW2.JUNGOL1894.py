'''
Created by: minseo
Date: 3/27/24
Desc : 정올 계단오르기
최대 2 칸 까지 오를 수 있을 때 오르는 방법의 가짓수를 출력 하는 문제
그림은 n 이 4 인 경우의 예
1 - 2 - 3 - 4
1 - 2 - 4
1 - 3 - 4
2 - 3 - 4
2 - 4
가짓수: 5가지
Excute time : 0.2102000ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

import sys

def step_recursive(left:int) -> int:
    if left == 0:
        # 더 못 올라갈 때
        return 1
    elif left==1:
        #한칸 더 올라갈 수 있을 때
        return step_recursive(left - 1)
    else:
        # 한칸이나 두칸 올라갈 수 있을 때
        return step_recursive(left - 1) + step_recursive(left - 2)


sys.stdin = open('03//JUNGOL1894.txt', 'r')
num = int(input())
print(step_recursive(num))
# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 시간: {(end_time - start_time) * 1000:.7f} milliseconds")
