from collections import deque


def bfs(start):
    queue = deque([start])
    visited[start] = 1
    while queue:
        now = queue.popleft()
        for to in graph[now]:
            if not visited[to]:
                visited[to] = visited[now] + 1
                queue.append(to)


for tc in range(1, 11):
    L, S = map(int, input().split())
    graph = [[] for _ in range(101)]
    call_node = list(map(int, input().split()))
    for i in range(len(call_node) // 2):
        if call_node[2*i + 1] not in graph[call_node[2*i]]:
            graph[call_node[2*i]].append(call_node[2*i + 1])

    visited = [0] * 101
    bfs(S)
    max_time = max(visited)
    max_list = []
    for i in range(1, 101):
        if visited[i] == max_time:
            max_list.append(i)

    res = max(max_list)
    print(f'#{tc} {res}')
