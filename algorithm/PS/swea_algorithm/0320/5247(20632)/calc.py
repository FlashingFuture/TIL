from collections import deque


def bfs(num):
    queue = deque([num])
    visited[num] = 1
    while queue:
        pos = queue.popleft()   # position
        if pos == M:
            return visited[pos]

        for n_pos in [pos + 1, pos - 1, pos * 2, pos - 10]:
            if 0 < n_pos <= 1000000 and not visited[n_pos]:
                queue.append(n_pos)
                visited[n_pos] = visited[pos] + 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    res = bfs(N) - 1
    print(f'#{tc} {res}')
