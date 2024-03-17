from collections import deque


def bfs(iy, ix):
    queue = deque([(iy, ix)])
    visited[iy][ix] = 1
    while queue:
        y, x = queue.popleft()
        for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and graph[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = 1


T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    for i in range(K):
        m, n = map(int, input().split())
        graph[n][m] = 1

    visited = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] and not visited[i][j]:
                bfs(i, j)
                cnt += 1

    print(cnt)
