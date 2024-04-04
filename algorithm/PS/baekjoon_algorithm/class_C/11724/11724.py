import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

# 그래프 탐색 : bfs
# 같은 연결 요소는 같은 visited값을 가지게 하는 형태로
# 총 연결 요소의 개수를 얻을 수 있음
visited = [0] * (N + 1)
cnt = 0
for i in range(1, N + 1):
    if visited[i] == 0:
        cnt += 1
        visited[i] = cnt
        queue = deque([i])
        while queue:
            pos = queue.popleft()
            if graph[pos]:
                for next_pos in graph[pos]:
                    if not visited[next_pos]:
                        queue.append(next_pos)
                        visited[next_pos] = 1

print(cnt)