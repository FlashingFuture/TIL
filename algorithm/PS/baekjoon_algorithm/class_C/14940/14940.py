from collections import deque


n, m = map(int, input().split())
chart = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
visited = [[-1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if chart[i][j] == 2:
            queue.append((i, j))
            visited[i][j] = 0

        if chart[i][j] == 0:
            visited[i][j] = 0

while queue:    # dfs
    y, x = queue.popleft()
    for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == -1:
            queue.append((ny, nx))
            visited[ny][nx] = visited[y][x] + 1

for i in range(n):
    for j in range(m):
        print(visited[i][j], end=" ")
    print()
