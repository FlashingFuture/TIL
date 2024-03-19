import sys
from collections import deque
input = sys.stdin.readline
dz = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dx = [0, 0, 0, 0, 1, -1]


M, N, H = map(int, input().split())
T = [[list(map(int, input().split())) for _ in range(N)] for __ in range(H)]
queue = deque([])
for i in range(H):
    for j in range(N):
        for k in range(M):
            if T[i][j][k] == 1:
                queue.append((i, j, k))

while queue:
    z, y, x = queue.popleft()
    for i in range(6):
        nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and T[nz][ny][nx] == 0:
            queue.append((nz, ny, nx))
            T[nz][ny][nx] = T[z][y][x] + 1


def result():
    temp = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if T[h][n][m] == 0:
                    return -1
                temp = max(temp, T[h][n][m])

    return temp - 1


res = result()
print(res)
