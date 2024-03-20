T = int(input())


def find_set(x):
    if parents[x] == x:
        return x

    return find_set(parents[x])


def union(x, y):
    root_x, root_y = find_set(x), find_set(y)
    if root_x == root_y:
        return

    if ranks[root_x] < ranks[root_y]:
        parents[root_x] = root_y
    else:
        parents[root_y] = root_x
        if ranks[root_x] == ranks[root_y]:
            ranks[root_x] += 1


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    parents = [i for i in range(N + 1)]
    ranks = [0 for _ in range(N + 1)]
    for i in range(0, M*2, 2):
        x, y = A[i], A[i + 1]
        union(x, y)

    res = len(set()) - 1
    print(f'#{tc} {res}')
