val = 123
temp = val

howmany = 0

# 총 자릿수를 세어서 temp에 대입
while temp:
    howmany += 1
    temp = temp//10

# str로 저장할 배열 생성
data = []

for i in range(howmany,0,-1):
    each = val % 10
    data.append(str(each))
    val = val//10
print(data)