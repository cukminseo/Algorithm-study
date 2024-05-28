import sys

# sys.stdin = open("BAJ10989.txt", "r")

freq = int(sys.stdin.readline())

count_arr = [0] * (10000+1)

for _ in range(freq):
    count_arr[int(sys.stdin.readline())]+=1

for i in range(10000+1):
    if count_arr:
        for j in range(count_arr[i]):
            print(i)

