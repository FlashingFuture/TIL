from heapq import heappop, heappush


def prim(start):
    visited = [0] * N
    pq = [(0, start)]
    total_cost = 0

    while pq:
        cost, node = heappop(pq)
        if visited[node]:
            continue

        visited[node] = 1
        total_cost += cost
        for n_node in graph[node]:
            if not visited[n_node]:
                n_cost = E * ((X[node] - X[n_node])**2 + (Y[node] - Y[n_node])**2)
                heappush(pq, (n_cost, n_node))

    return total_cost


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    graph = [[i for i in range(N) if i != _] for _ in range(N)]
    res = prim(0)
    print(f'#{tc} {res:.0f}')
