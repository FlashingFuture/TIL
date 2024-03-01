path = []


def backtrack(lev):
    if lev == M:
        print(*path)
        return
    
    for i in range(1, N + 1):
        if i in path: continue
        path.append(i)
        backtrack(lev + 1)
        path.pop()


N, M = map(int, input().split())

backtrack(0)