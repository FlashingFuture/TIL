def order(n):
    visited[n] = 1
    if graph[n]:
        for item in graph[n]:
            if not visited[item]:
                global cnt
                cnt += 1
                order(item)


N = int(input())                        # 컴퓨터의 수
n_nodes = int(input())                  # 간선의 수
graph = [[] for _ in range(N + 1)]          # 그래프 선언
for i in range(n_nodes):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [0] * (N + 1)
cnt = 0
order(1)
print(cnt)