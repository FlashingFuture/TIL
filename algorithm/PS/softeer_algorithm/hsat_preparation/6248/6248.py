n, m = map(int, input().split())
graph = [[] for _ in range(m)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)

S, T = map(int, input().split())
