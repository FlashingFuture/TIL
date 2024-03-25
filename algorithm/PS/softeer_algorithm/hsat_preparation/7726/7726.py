import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())
chart = [sys.stdin.readline() for _ in range(n)]
# N: 시작위치 D: 출구 G: 유령 #: 벽 .:빈공간
# 유령이 출구에 이르는 속도보다 남우가 빨라야만 탈출이 가능
start, goal = (0, 0), (0, 0)
ghosts = []
visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if chart[i][j] == 'N':
            start = (i, j)

        elif chart[i][j] == 'D':
            goal = (i, j)

        elif chart[i][j] == 'G':
            ghosts.append((i, j))

        elif chart[i][j] == '#':
            visited[i][j] = 1

max_min_time = sys.maxsize
for ghost in ghosts:
    temp_diff = abs(ghost[0] - goal[0]) + abs(ghost[1] - goal[1])
    max_min_time = min(temp_diff, max_min_time)

queue = deque([start])
visited[start[0]][start[1]] = 1

while queue:
    y, x = queue.popleft()
    for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
            queue.append((ny, nx))
            visited[ny][nx] = visited[y][x] + 1

for i in range(n):
    print(visited[i])


if visited[goal[0]][goal[1]] <= max_min_time and visited[goal[0]][goal[1]]:
    print('Yes')
else:
    print('No')
