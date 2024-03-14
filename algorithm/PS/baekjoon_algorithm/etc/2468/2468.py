from collections import deque


N = int(input())
chart = [list(map(int, input().split())) for _ in range(N)]
max_r = 0
for i in range(N):
    for j in range(N):
        if max_r < chart[i][j]:
            max_r = chart[i][j]


def bfs(y, x):
    queue = deque([(y, x)])     # bfs 시작 위치
    while queue:
        y, x = queue.popleft()
        for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and chart[ny][nx] > k:
                queue.append((ny, nx))
                visited[ny][nx] = 1


res = 0
for k in range(max_r):
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and chart[i][j] > k:
                bfs(i, j)
                cnt += 1

    if res < cnt:
        res = cnt

print(res)
