from collections import deque


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    chart = [list(map(int, input().split())) for _ in range(N)]
    # 커버가 되는 집은 중심점을 기준으로 최대 (K-1)만큼 떨어진 점
    res = 0
    for k in range(1, 22):  # 225 + 196 > 400이므로 최대 15
        max_house = 0
        for i in range(N):
            for j in range(N):
                length = k - 1
                queue = deque([(i, j, length)])
                visited = [[0] * N for _ in range(N)]
                visited[i][j] = 1
                temp_house = 0
                while queue:
                    y, x, length_left = queue.popleft()
                    if chart[y][x]:
                        temp_house += 1
                    if length_left:
                        for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
                            ny, nx = y + dy, x + dx
                            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                                visited[ny][nx] = 1
                                queue.append((ny, nx, length_left - 1))

                max_house = max(max_house, temp_house)

        if max_house * M >= 2*(k**2) - 2*k + 1:
            res = max_house

    print(f'#{tc} {res}')
