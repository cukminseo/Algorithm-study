'''
Created by: minseo
Date: 4/17/24
Desc : 
Excute time : ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

Data = "1+2*3+(4+5)/6";
isp = {'*':2, '/':2, '+':1, '-':1, '(':0}
icp = {'*':2, '/':2, '+':1, '-':1, '(':3}

stack = []
PostFix = []

for now in Data:
    if '0'<=now<='9':
        PostFix.append(now)
    elif now == ')':
        while stack[-1]!='(':
            PostFix.append(stack.pop())
        stack.pop()
    else :
        if not stack:
            stack.append(now)
        elif icp[now] > isp[stack[-1]]:
            stack.append(now)
        else :
            while stack and isp[stack[-1]] >= icp[now]:
                PostFix.append(stack.pop())
            stack.append(now)
while stack : PostFix.append(stack.pop())
print(PostFix)

for now in PostFix:
    if now.isdigit():
        stack.append(now)

    else:
        b = int(stack.pop())
        a = int(stack.pop())

        if now == '*':
            stack.append(a*b)
        elif now == '/':
            stack.append(a/b)
        elif now == '+':
            stack.append(a+b)
        elif now == '-':
            stack.append(a-b)
print(stack[-1])

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
