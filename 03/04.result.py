'''
Created by: minseo
Date: 3/27/24
Desc : 
Excute time : ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

ans = 0
digit = 1
def GetSome(num):
    global ans
    global digit
    if num > 0:
        GetSome(int(num / 10))
        ans += (num % 10) * digit
        digit *= 10
    return

GetSome(321)
print(ans)


# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
