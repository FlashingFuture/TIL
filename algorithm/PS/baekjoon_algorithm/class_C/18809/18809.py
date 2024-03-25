from collections import deque


path = []


def backtrack(lev_r, lev_g, lev_x):
    if len(path) == len(W):
        visited = [[0] * M for _ in range(N)]
        queue = deque([])
        for lev in range(len(path)):
            if path[lev] == 1:
                queue.append(W[lev])
                visited[W[lev][0]][W[lev][1]] = -1

        for lev in range(len(path)):
            if path[lev] == 2:
                queue.append(W[lev])
                visited[W[lev][0]][W[lev][1]] = 1

        f_cnt = 0
        while queue:
            y, x = queue.popleft()
            for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M and chart[ny][nx] and visited[ny][nx] == 0:
                    if visited[y][x] < 0:
                        visited[ny][nx] = visited[y][x] - 1
                        queue.append((ny, nx))
                    elif 0 < visited[y][x] < 999:
                        visited[ny][nx] = visited[y][x] + 1
                        queue.append((ny, nx))

                if 0 <= ny < N and 0 <= nx < M and chart[ny][nx] and visited[ny][nx] + visited[y][x] == -1:
                    visited[ny][nx] = 999
                    f_cnt += 1

        global res
        res = max(f_cnt, res)
        return

    if lev_x < X:
        path.append(0)
        backtrack(lev_r, lev_g, lev_x + 1)
        path.pop()

    if lev_r < R:
        path.append(1)
        backtrack(lev_r + 1, lev_g, lev_x)
        path.pop()

    if lev_g < G:
        path.append(2)
        backtrack(lev_r, lev_g + 1, lev_x)
        path.pop()


N, M, G, R = map(int, input().split())
chart = [list(map(int, input().split())) for _ in range(N)]
W = []      # 배양액을 뿌릴 위치를 저장할 리스트
for i in range(N):
    for j in range(M):
        if chart[i][j] == 2:
            W.append((i, j))


X = len(W) - G - R
res = 0
backtrack(0, 0, 0)
print(res)
