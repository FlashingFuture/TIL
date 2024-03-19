def backtrack(lev, cost):
    global min_cost
    if min_cost <= cost:
        return

    if lev == N:
        min_cost = cost
        return

    for i in range(N):
        if i in path: continue
        path.append(i)
        backtrack(lev + 1, cost + V[lev][i])
        path.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    path = []
    min_cost = 99 * 15
    backtrack(0, 0)
    print(f'#{tc} {min_cost}')
