# https://www.acmicpc.net/problem/2623


import sys
from collections import deque


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
for _ in range(M):
    data = list(map(int, input().split()))
    for i in range(1, len(data) - 1):
        graph[data[i]].append(data[i + 1])
        in_degree[data[i + 1]] += 1


q = deque()
result = []

for i in range(1, N + 1):
    if in_degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)
    for next_singer in graph[now]:
        in_degree[next_singer] -= 1
        if in_degree[next_singer] == 0:
            q.append(next_singer)

if len(result) == N:
    for singer in result:
        print(singer)

else:
    print(0)