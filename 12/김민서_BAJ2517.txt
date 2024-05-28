import sys
sys.stdin = open("BAJ2517.txt", "r")

n = int(input().strip())
arr = list(map(int, input().strip().split()))
answer = 0

def merge_sort(data, temp, left, right):
    global answer
    if left < right:
        mid = (left + right) // 2
        merge_sort(data, temp, left, mid)
        merge_sort(data, temp, mid + 1, right)
        merge(data, temp, left, mid, right)

def merge(data, temp, left, mid, right):
    global answer
    i = left
    j = mid + 1
    k = left

    while i <= mid and j <= right:
        if data[i] <= data[j]:
            temp[k] = data[i]
            i += 1
        else:
            temp[k] = data[j]
            answer += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp[k] = data[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = data[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        data[i] = temp[i]

temp = [0] * n
merge_sort(arr, temp, 0, n - 1)
print(answer)
