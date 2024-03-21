from heapq import heappush, heappop


def dijkstra(start):
    pq = [(0, start)]
    while pq:
        time, node = heappop(pq)

        for move in graph[node]:
            n_time, n_node = move
            next_time = time + n_time
            if distance[n_node] > next_time:
                distance[n_node] = next_time
                heappush(pq, (next_time, n_node))


T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        graph[x].append((c, y))

    max_time = 0
    for i in range(1, N + 1):
        if i == X: continue
        distance = [100000000] * (N + 1)
        dijkstra(i)
        temp = distance[X]
        distance = [100000000] * (N + 1)
        dijkstra(X)
        temp += distance[i]
        max_time = max(max_time, temp)

    print(f'#{tc} {max_time}')
