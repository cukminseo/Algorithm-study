'''
소수판별
'''
import time

# 측정 시작
start_time = time.perf_counter()

num = 11
# flag
isPrime = True

for now in range(2, num//2+1):
    if num % now == 0:
        isPrime = False

print()

# 측정 종료 시간
end_time = time.perf_counter()

# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time)*1000:.5f} milliseconds")