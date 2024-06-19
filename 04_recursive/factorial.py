def fact(num):
    if num > 1:
        return num * fact(num - 1)
    else:
        return 1

num=int(input())
print(fact(num))
