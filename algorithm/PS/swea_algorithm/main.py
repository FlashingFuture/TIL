path = []
res_list = []


def backtrack(lev):
    if lev == N:
        temp = P[0][path[0]] / 100
        for i in range(1, N):
            temp *= P[i][path[i]] / 100

        res_list.append(temp)
        return

    for i in range(N):
        if i in path: continue
        path.append(i)
        backtrack(lev + 1)
        path.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    res_list = []
    backtrack(0)
    res = max(res_list)
    print(f'#{tc} {res}')

