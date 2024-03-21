from heapq import heappop, heappush
T = int(input())


def dijkstra(start):
    pq = []
    heappush(pq, (0, start))
    distance[start] = 0
    while pq:
        dist, pos = heappop(pq)

        for move in graph[pos]:
            next_weight, next_pos = move[0], move[1]

            next_dist = dist + next_weight
            if next_dist < distance[next_pos]:
                distance[next_pos] = next_dist
                heappush(pq, (next_dist, next_pos))


for tc in range(1, T + 1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))

    distance = [2**31] * (N + 1)
    dijkstra(0)
    res = distance[N]
    print(f'#{tc} {res}')
