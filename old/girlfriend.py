import sys


def get_some(node):
    global mincost, cost

    # 너무 깊게 탐색하지 않도록 조절
    if mincost < cost:
        return

    # 탈출
    if node == map_size:
        if mincost > cost:
            mincost = cost
        return

    for next_node in range(1, map_size + 1):
        if graph[node][next_node] and not visited[next_node]:
            visited[next_node] = 1
            cost += graph[node][next_node]
            get_some(next_node)
            # 흔적 지우기
            cost -= graph[node][next_node]
            visited[next_node] = 0


sys.stdin = open('GF.txt', 'r')

map_size, link_count = map(int, input().split())

graph = [[0 for _ in range(map_size + 1)] for _ in range(map_size + 1)]
visited = [0 for _ in range(map_size + 1)]

# input
for _ in range(link_count):
    a, b, cost = map(int, input().split())
    graph[a][b] = cost
    graph[b][a] = cost

mincost = 9999
cost = 0
start = 1
visited[start] = 1
get_some(node=start)

print(mincost)
