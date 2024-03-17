from collections import deque


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)


for item in graph:
    item.sort()
# DFS
visited = [0] * (N + 1)


def dfs(v):
    print(v, end=' ')
    visited[v] = 1
    for item in graph[v]:
        if not visited[item]:
            dfs(item)


dfs(V)
print()
# BFS
queue = deque([V])
visited = [0] * (N + 1)
visited[V] = 1
while queue:
    x = queue.popleft()
    print(x, end=' ')

    for item in graph[x]:
        if not visited[item]:
            queue.append(item)
            visited[item] = 1
