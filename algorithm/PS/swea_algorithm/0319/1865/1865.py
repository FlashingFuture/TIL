def backtrack(lev, pro):    # pro: probability
    global min_pro
    if pro < min_pro:
        return

    if lev == N:
        min_pro = pro
        return

    for i in range(N):
        if i in path: continue
        if P[lev][i] == 0: continue
        path.append(i)
        backtrack(lev + 1, pro * P[lev][i] / 100)
        path.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    path = []
    res_list = []
    min_pro = 0
    backtrack(0, 1)
    res = min_pro * 100

    print(f'#{tc} {res:.6f}')
