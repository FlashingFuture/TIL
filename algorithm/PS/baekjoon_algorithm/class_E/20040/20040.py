import sys


if __name__ == '__main__':
    n, m = map(int, input().split())
    parent = [i for i in range(n)]
    rank = [0] * n


    def find(x):
        if x == parent[x]:
            return x
        else:
            y = find(parent[x])
            parent[x] = y
            return y


    def union(x, y):
        r1 = find(x)
        r2 = find(y)

        if rank[r1] > rank[r2]:
            parent[r2] = r1
        elif rank[r1] < rank[r2]:
            parent[r1] = r2
        else:
            parent[r2] = r1
            rank[r1] += 1

    answer = 0
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if find(a) == find(b):
            answer = i + 1
            break

        union(a, b)

    print(answer)


# 풀이
# disjoint set 활용
