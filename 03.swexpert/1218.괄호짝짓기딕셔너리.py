'''
Created by: minseo
Date: 4/3/24
Desc : SWEA1218
Excute time : ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

pare = {'>': '<', ')': '(', ']': '[', '}': '{'}
data = ['<', '{', '}', '>']

stack = []
ans = 0
isCorrect = True
while data:
    now = data.pop(0)
    if now in pare.values():
        # 여는 괄호라면
        stack.append(now)
    else:
        if not stack or stack[-1] != pare[now]:
            isCorrect = False
            break
        stack.pop()

if not stack and isCorrect:
    print('YES')
else:
    print('NO')



print()

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
