'''
Created by: minseo
Date: 3/20/24
Desc : 
Excute time : ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()


def is_safe(y: int, x: int) -> bool:
    return 0 <= x < 5 and 0 <= y < 5


def myAbs(a:int) -> int:
    return a if a > 0 else -a


data = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

y = 0
x = 0

sum = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        for direction in range(4):
            newY = y + dy[direction]
            newX = y + dx[direction]
            if is_safe(newY, newX):
                sum += myAbs(data[y][x]-data[newY][newX])


# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
