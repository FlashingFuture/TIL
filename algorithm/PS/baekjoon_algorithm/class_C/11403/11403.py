from collections import deque


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]


def bfs(start):
    queue = deque([start])
    while queue:
        pos = queue.popleft()
        for x in range(N):
            if graph[pos][x] == 1 and not visited[start][x]:
                queue.append(x)
                visited[start][x] = 1


for i in range(N):
    bfs(i)


for i in range(N):
    print(*visited[i])
