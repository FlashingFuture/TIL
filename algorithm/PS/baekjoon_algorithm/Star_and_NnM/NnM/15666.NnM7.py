N, M = map(int, input().split())
A = list(map(int, input().split()))
A = list(set(A))
N = len(A)
A.sort()
path = []


def backtrack(lev, start):
    if lev == M:
        print(*path)
        return

    for i in range(start, N):
        path.append(A[i])
        backtrack(lev + 1, i)
        path.pop()


backtrack(0, 0)
