def find_set(parents, x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]


def union(ranks, parents, x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if ranks[root_x] < ranks[root_y]:
        parents[root_x] = root_y

    elif ranks[root_x] > ranks[root_y]:
        parents[root_y] = root_x

    else:
        parents[root_y] = root_x
        ranks[root_x] += 1


def kruskal():
    result = []
    graph.sort(key=lambda x: x[-1])     # 가중치 오름차순
    parents = []
    ranks = []

    for node in range(V + 1):
        parents.append(node)
        ranks.append(0)

    i, e = 0, 0
    while e < V:
        n1, n2, w = graph[i]
        i = i + 1
        x = find_set(parents, n1)
        y = find_set(parents, n2)
        if x != y:
            e = e + 1
            result.append(w)
            union(parents, ranks, x, y)

    return i


T = int(input())
for tc in range(1, T+1):
    # V : 가장 마지막 노드 번호
    V, E = map(int, input().split())
    # 0부터 시작하므로...
    graph = []
    for _ in range(E):
        graph.append(list(map(int, input().split())))

    res = kruskal()
    print(f'#{tc} {res}')