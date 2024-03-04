path = []


def backtrack(n):
    if n == M:
        print(*path)
        return

    for i in range(1, N + 1):
        if path and i < path[-1]: continue
        path.append(i)
        backtrack(n + 1)
        path.pop()


N, M = map(int, input().split())
backtrack(0)