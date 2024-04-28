# mst 문제 : 지난번에 prim 으로 풀었으니 이번엔 kruskal
def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y:
        return

    if root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y


V, E = map(int, input().split())
edges = []
for _ in range(E):
    s, e, w = map(int, input().split())     # start, end, weight
    edges.append((s, e, w))

edges.sort(key=lambda x: x[2])      # weight 에 대해 sort
parents = [i for i in range(V + 1)]     # 전체 원소에 대한 부모 배열
total_weight = 0
for s, e, w in edges:
    # cycle 이 발생하지 않도록 같은 집합인 경우 continue
    if find_set(s) == find_set(e):
        continue

    union(s, e)
    total_weight += w

print(total_weight)
