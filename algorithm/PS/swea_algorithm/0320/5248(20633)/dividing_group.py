from collections import deque


def bfs(start):
    visited[start] = 1
    queue = deque([start])
    while queue:
        pos = queue.popleft()
        for item in graph[pos]:
            if not visited[item]:
                queue.append(item)
                visited[item] = 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    forms = list(map(int, input().split()))
    for i in range(M):
        graph[forms[2*i]].append(forms[2*i + 1])
        graph[forms[2*i + 1]].append(forms[2*i])

    visited = [0] * (N + 1)
    cnt = -1    # 0을 visited해주기에 -1부터 셈
    for i in range(N + 1):
        if not visited[i]:
            bfs(i)
            cnt += 1

    print(f'#{tc} {cnt}')
