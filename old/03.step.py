'''
Created by: minseo
Date: 4/3/24
Desc : 
Excute time : ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

ans = 0


def get_sum(here: int):
    global ans
    if here > howmany: return
    if here == howmany:
        ans += 1
        return
    get_sum(here + 1)
    get_sum(here + 2)


howmany = int(input())
get_sum(0)
print(ans)

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
