'''
Created by: minseo
Date: 4/16/24
Desc : SWEA 12712(파리퇴치3)
Excute time : ms(time.perf_counter())
'''
import sys

sys.stdin = open('SWEA 12712. 파리퇴치3.txt', 'r')

# 상 하 좌 우
plus_dx = [0, 0, -1, 1]
plus_dy = [1, -1, 0, 0]
# 10 2 4 8
x_dx = [-1, 1, 1, -1]
x_dy = [1, 1, -1, -1]

# for문으로 한번에 진행하기 위해 합치기
plus_x_dx = []
plus_x_dy = []
plus_x_dx.append(plus_dx)
plus_x_dx.append(x_dx)
plus_x_dy.append(plus_dy)
plus_x_dy.append(x_dy)

tc = int(input())

for case in range(1, tc+1):

    matrix_size, spray_size = map(int, input().split())

    # 상태저장 그래프
    graph = [[0 for _ in range(matrix_size)] for __ in range(matrix_size)]
    # 결과저장 그래프
    result = [[-1 for _ in range(matrix_size)] for __ in range(matrix_size)]

    for i in range(matrix_size):
        graph[i] = list(map(int, input().split()))

    # 완전 탐색
    for i in range(matrix_size):
        for j in range(matrix_size):
            # 두가지 스프레이 방식
            for method in range(2):
                sum = 0
                sum += graph[j][i]
                # 스프레이 분사된 부분의 합
                for spray_depth in range(1, spray_size):
                    # 4가지 방향 탐색
                    for arrow in range(4):
                        new_y = j+plus_x_dy[method][arrow] * spray_depth
                        new_x = i+plus_x_dx[method][arrow] * spray_depth
                        # 범위를 넘는지 검사
                        if 0 <= new_y < matrix_size and 0 <= new_x < matrix_size:
                            sum += graph[new_y][new_x]
                # 스프레이 합 결과 확인 후 반영
                result[j][i] = max(result[j][i], sum)

    max_value = max(map(max, result))
    print(f"#{case} {max_value}")