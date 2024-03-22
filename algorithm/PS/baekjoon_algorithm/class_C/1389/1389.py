from collections import deque


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    queue = deque([start])
    kb_cnt = 0      # kevin bacon counter
    while queue:
        pos = queue.popleft()
        kb_cnt += (kb_visited[pos] - 1)
        for n_pos in graph[pos]:
            if not kb_visited[n_pos]:
                queue.append(n_pos)
                kb_visited[n_pos] = kb_visited[pos] + 1

    return kb_cnt


min_kb = 250000000
min_personnel = 0
for i in range(1, N + 1):
    kb_visited = [0] * (N + 1)
    temp_kb = bfs(i)
    if temp_kb < min_kb:
        min_personnel = i
        min_kb = temp_kb

print(min_personnel)
