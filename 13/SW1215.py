
import time

# 측정 시작
start_time = time.perf_counter()

import sys

sys.stdin = open('SW1215.txt', 'r')

def isPalin(y,x):
    for now in range(howmany//2):
        if data[y][x+now]!=data[y][x+howmany-1-now]:
            return False
    return True

howmany = int(input())

data = [0]*8
for i in range(8):
    data[i] = list(input())

ans = 0
for y in range(8):
    for x in range(8-howmany+1):
        if isPalin(y,x):
            ans+=1

for y in range(8):
    for x in range(8):
        if y>x:
            data[y][x], data[x][y] = data[x][y], data[y][x]

for y in range(8):
    for x in range(8-howmany+1):
        if isPalin(y,x):
            ans+=1

print(ans)
# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
