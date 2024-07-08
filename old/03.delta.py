'''
Created by: minseo
Date: 3/20/24
Desc : 
Excute time : ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

data = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 이게 예의
whereY = -1
whereX = -1

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 13:
            whereY = y
            whereX = x
        # 여기서 굳이 break를 써도 하나 루트만 나올 수 있고, 빠져 나와 봤자 같은 n^2
        # 굳이 한번에 빠져나오고 싶으면 함수화 해서 return으로 한번에 나올 수 있을 듯 하다

print(whereY, whereX)

# for (x_bias, y_bias) in zip(dx, dy):
#     print(data[whereY+y_bias][whereX+x_bias])

for i in range(4):
    newY = whereY + dy[i]
    newX = whereX + dx[i]
    if 0 <= newY < 5 and 0 <= newX < 5:
        print(data[newY][newX])
    else:
        print(-1)

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
