from collections import deque


M, N = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(N)]
queue = deque([])
for i in range(N):
    for j in range(M):
        if boxes[i][j] == 1:
            queue.append((i, j))

while queue:
    y, x = queue.popleft()
    for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and not boxes[ny][nx]:
            queue.append((ny, nx))
            boxes[ny][nx] = boxes[y][x] + 1


def result():
    temp = 0
    for n in range(N):
        for m in range(M):
            if boxes[n][m] == 0:
                return -1
            temp = max(temp, boxes[n][m])

    return temp - 1


res = result()
print(res)