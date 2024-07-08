'''
data.reverse() 구현
'''


data = [i for i in range(1, 7)]
data_len = len(data)

for i in range(data_len):
    data[i], data[data_len-i] = data[data_len-i], data[i]

print(data)
