from collections import deque


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)

# DFS
stack = [V]
visited = [0] * (N + 1)
while stack:
    x = stack.pop()
    if not visited[x]:
       print(x, end=' ')
    visited[x] = 1
    for item in graph[x]:
        if not visited[item]:
            stack.append(x)
            stack.append(item)
            break

print()
# BFS
queue = deque([V])
visited = [0] * (N + 1)
while queue:
    x = queue.popleft()
    if not visited[x]:
        print(x, end=' ')

    visited[x] = 1
    for item in graph[x]:
        if not visited[item]:
            queue.append(item)