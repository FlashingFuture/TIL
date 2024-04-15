# 아마도 MST 문제 : prim 알고리즘과 친해지기
from heapq import heappush, heappop


n = int(input())
x, y = [0.0] * 101, [0.0] * 101
for i in range(1, n + 1):
    x[i], y[i] = map(float, input().split())

# 관계그래프 작성
graph = [[] for _ in range(101)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            continue
        distance = ((x[i] - x[j])**2 + (y[i] - y[j])**2)**(1/2)  # sqrt쓸?까
        graph[i].append((distance, j))


def prim(start):
    pq = []
    total_weight = 0
    heappush(pq, (0, start))    # weight은 0에서 시작
    visited = [0] * 101
    while pq:
        weight, pos = heappop(pq)
        if visited[pos]: continue
        visited[pos] = 1
        total_weight += weight
        for next_pos in graph[pos]:
            if not visited[next_pos[1]]:
                heappush(pq, next_pos)

    return total_weight


res = prim(1)
print(f'{res:.2f}')
