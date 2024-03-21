from heapq import heappush, heappop


def dijkstra(y, x):
    pq = []
    heappush(pq, (0, y, x))
    while pq:
        cost, ny, nx = heappop(pq)      # nowy, nowx

        for move in graph[ny][nx]:
            next_weight = move[0]
            next_y, next_x = move[1], move[2]
            next_cost = cost + next_weight
            if min_cost[next_y][next_x] > next_cost:
                min_cost[next_y][next_x] = next_cost
                heappush(pq, (next_cost, next_y, next_x))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]
    graph = [[[] for _ in range(N)] for __ in range(N)]
    for i in range(N):
        for j in range(N):
            for di, dj in (1, 0), (-1, 0), (0, 1), (0, -1):
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    diff = H[ni][nj] - H[i][j]
                    if diff < 0:
                        diff = 0
                    diff += 1       # 기본 연료 소비량 1 추가
                    graph[i][j].append((diff, ni, nj))

    min_cost = [[100000000] * N for _ in range(N)]
    dijkstra(0, 0)
    res = min_cost[N - 1][N - 1]
    print(f'#{tc} {res}')
