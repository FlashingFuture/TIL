from heapq import heappop, heappush


def dijkstra(start_y, start_x):
    pq = []
    heappush(pq, (0, start_y, start_x))
    min_time[start_y][start_x] = 0
    while pq:
        time, y, x = heappop(pq)
        for move in graph[y][x]:
            n_time, ny, nx = move      # new
            next_time = time + n_time
            if min_time[ny][nx] > next_time:
                min_time[ny][nx] = next_time
                heappush(pq, (next_time, ny, nx))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    chart = [input() for _ in range(N)]                     # 실제 지도
    graph = [[[] for _ in range(N)] for __ in range(N)]     # 자리마다 델타이동시 복구량을 저장한 그래프
    for i in range(N):
        for j in range(N):
            for di, dj in (1, 0), (-1, 0), (0, 1), (0, -1):
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    graph[i][j].append((int(chart[ni][nj]), ni, nj))

    min_time = [[2**31] * N for _ in range(N)]
    dijkstra(0, 0)
    res = min_time[N - 1][N - 1]
    print(f'#{tc} {res}')
