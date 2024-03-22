from collections import deque


def bfs(start):
    queue = deque([start])
    visited[start] = 1
    while queue:
        pos = queue.popleft()
        for next_pos in graph[pos]:
            if not visited[next_pos]:
                queue.append(next_pos)
                visited[next_pos] = visited[pos] + 1


for tc in range(1, 11):
    N, S = map(int, input().split())
    from_to = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    for i in range(0, len(from_to), 2):
        graph[from_to[i]].append(from_to[i + 1])

    visited = [0] * 101
    bfs(S)
    max_idx = 0
    max_num = 0
    for idx in range(101):
        if max_num <= visited[idx]:
            max_idx = idx
            max_num = visited[idx]

    print(f'#{tc} {max_idx}')
