import sys
from collections import deque


N = int(sys.stdin.readline())
pic = [sys.stdin.readline() for _ in range(N)]
visited = [[0] * N for _ in range(N)]


def bfs(y_input, x_input):
    queue = deque([(y_input, x_input)])
    while queue:
        y, x = queue.popleft()
        for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and pic[ny][nx] == pic[y][x]:
                queue.append((ny, nx))
                visited[ny][nx] = 1


cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt += 1

# 이제, 세상을 적록색약의 관점으로 바라보자
for i in range(N):
    temp_str = ''
    for item in pic[i]:
        if item == 'R':   # 적색약으로 가정
            temp_str += 'G'
        else:
            temp_str += item

    pic[i] = temp_str


visited = [[0] * N for _ in range(N)]
cnt_cb = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt_cb += 1

print(cnt, cnt_cb)
