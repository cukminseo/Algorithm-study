'''
Created by: minseo
Date: 4/17/24
Desc : 
Excute time : ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

import sys

sys.stdin = open("01.zombie_dfs.txt", "r")


def GetSome(here):
    if here > Zombie: return
    for i in ability:
        next = here + i
        if Time[next] > Time[here] + 1:
            Time[next] = Time[here] + 1
            GetSome(next)


ability = [0] * 3
Time = [987654321] * 100000
Shalala, Zombie = map(int, input().split())

ability[0], ability[1], ability[2] = map(int, input().split())

Time[Shalala] = 0

if Shalala == Zombie:
    print(0)

else:
    GetSome(Shalala)

if Time[Zombie] != 987654321:
    print(Time[Zombie])

else:
    print(-1)

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
