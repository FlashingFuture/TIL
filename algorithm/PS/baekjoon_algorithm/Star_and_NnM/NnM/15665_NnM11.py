N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr = list(set(arr))
arr.sort()
path = []


def backtrack():
    if len(path) == M:
        print(*path)
        return

    for num in arr:
        path.append(num)
        backtrack()
        path.pop()


backtrack()