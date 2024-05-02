# 2차원 union find 를 해서
# 전체 집합의 개수를 구하면 될듯

def union(y, x):
    if parents[y][x] == (y, x):
        return y, x

    parents[y][x] = parents[parents[y][x][0]][parents[y][x][1]]
    return parents[y][x]


def find(y1, x1, y2, x2):
    root_1 = parents[y1][x1]
    root_2 = parents[y2][x2]


N, M = map(int, input().split())
direction = [input() for _ in range(N)]
parents = [[''] * M for _ in range(N)]
