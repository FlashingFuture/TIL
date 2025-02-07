# https://www.acmicpc.net/problem/1753


import sys
from heapq import heappush, heappop

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

distance = [sys.maxsize] * (V + 1)
distance[K] = 0
pq = []
heappush(pq, (0, K))
while pq:
    dist, now = heappop(pq)
    if distance[now] < dist:
        continue

    for next, weight in graph[now]:
        cost = dist + weight
        if cost < distance[next]:
            distance[next] = cost
            heappush(pq, (cost, next))


for i in range(1, V + 1):
    if distance[i] == sys.maxsize:
        print("INF")
    else:
        print(distance[i])