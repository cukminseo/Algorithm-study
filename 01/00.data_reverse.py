data = [i for i in range(1,7)]
howmany = len(data)

for i in range(howmany):
    data[i], data[howmany-i] = data[howmany-i], data[i]

print(data)
