import sys


path = []


def backtrack(lev):
    if lev == M:
        print(*path)
        return

    for i in range(N):
        if path and seq[i] < path[-1]: continue
        path.append(seq[i])
        backtrack(lev + 1)
        path.pop()


N, M = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))
seq.sort()
backtrack(0)