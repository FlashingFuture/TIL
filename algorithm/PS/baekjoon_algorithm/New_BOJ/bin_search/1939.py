# https://www.acmicpc.net/problem/1939


import sys
from collections import deque

# 입력
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
max_weight = 0

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    max_weight = max(max_weight, c)

start, end = map(int, input().split())

# 가능한지 확인하는 함수
def is_possible(limit):
    visited = [False] * (N + 1)
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        current = queue.popleft()
        if current == end:
            return True
        for next_node, weight in graph[current]:
            if not visited[next_node] and weight >= limit:
                visited[next_node] = True
                queue.append(next_node)
    return False

# 이분 탐색
low = 1
high = max_weight
answer = 0

while low <= high:
    mid = (low + high) // 2
    if is_possible(mid):
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)