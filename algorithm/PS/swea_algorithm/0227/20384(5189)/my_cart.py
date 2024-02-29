def recur(n):
    if len(path) == N:
        total = 0
        count = [0] * N
        for i in range(N):
            if i == path[i]: return
            total += arr[i][path[i]]

        print(path)
        total_list.append(total)
        return

    for i in range(N):
        if i in path: continue
        path.append(i)
        recur(i)
        path.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    path = []
    total_list = []
    recur(0)
    print(total_list)