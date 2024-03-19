val = 123
temp = val

val_len = 0

# 총 자릿수를 세어서 temp에 대입
while temp:
    val_len += 1
    temp = temp//10

# str로 저장할 배열 생성
data = []

for i in range(val_len,0,-1):
    each = val % 10
    data.append(str(each))
    val = val//10
print(data)