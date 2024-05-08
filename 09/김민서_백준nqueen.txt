def get_some(y):
    global ans
    if y > howmany:
        ans += 1
        return
    for x in range(1, howmany + 1):
        if not visited[x] and not visited_increase[y + x] and not visited_decrease[y - x + howmany]:
            visited[x] = visited_increase[y + x] = visited_decrease[y - x + howmany] = 1
            get_some(y + 1)
            visited[x] = visited_increase[y + x] = visited_decrease[y - x + howmany] = 0


howmany = int(input())

visited = [0] * (howmany + 1)
visited_increase = [0] * (2 * howmany + 1)
visited_decrease = [0] * (2 * howmany + 1)
ans = 0

get_some(1)
print(ans)
