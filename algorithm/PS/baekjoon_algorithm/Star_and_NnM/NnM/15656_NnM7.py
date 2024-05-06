path = []


def backtrack(lev, start):
    if lev == M:
        print(*path)
        return

    for i in range(start, N):
        path.append(arr[i])
        backtrack(lev + 1, start)
        path.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
backtrack(0, 0)
