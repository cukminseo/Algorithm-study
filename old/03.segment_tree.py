'''
Created by: minseo
Date: 6/5/24
Desc : 
'''
import time

# 측정 시작
start_time = time.perf_counter()


def build():
    for i in range(howmany):
        tree[howmany + i] = a[i]

    for i in range(howmany - 1, 0, -1):
        tree[i] = tree[i << 1] + tree[i << 1 | 1]
    print(tree)


def update_tree(where, value):
    where += howmany
    tree[where] = value

    while where > 1:
        tree[where >> 1] = tree[where] + tree[where ^ 1]
        where >>= 1


def query(left, right):
    sum = 0
    left += howmany
    right += howmany
    while left<=right:
        if (left & 1):
            sum += tree[left]
            left += 1
        if not (right & 1):
            sum += tree[right]
            right -= 1
        left>>=1
        right>>=1
    return sum



a = [1, 2, 3, 4, 5]
howmany = len(a)
tree = [0] * (2 * howmany)
build()

update_tree(2, 1)
print(tree)

print(query(1,3))
# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
