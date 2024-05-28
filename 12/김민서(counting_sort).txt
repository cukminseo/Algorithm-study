data = [0, 4, 1, 3, 1, 2, 4, 1]

count_arr = [0] * (max(data)+1)

for i in data:
    count_arr[i]+=1

new_data = []
for num, count in enumerate(count_arr):
    new_data += [num] * count

print(new_data)