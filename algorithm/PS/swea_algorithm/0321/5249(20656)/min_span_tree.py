from heapq import heappop, heappush


def prim(start):
    pq = []
    visited = [0] * (V + 1)

    heappush(pq, (0, start))
    sum_weight = 0
    cnt = 0

    while pq and cnt <= V:
        weight, pos = heappop(pq)
        if visited[pos]:
            continue

        visited[pos] = 1
        cnt += 1
        sum_weight += weight
        for next_pos in graph[pos]:
            if not visited[next_pos[1]]:
                heappush(pq, next_pos)

    return sum_weight


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph[n1].append((w, n2))
        graph[n2].append((w, n1))

    res = prim(0)
    print(f'#{tc} {res}')
