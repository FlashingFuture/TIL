R, C, T = map(int, input().split())
chart = [list(map(int, input().split())) for _ in range(R)]
# 최대 크기는 50X50으로 완전탐색을 통한 확산 진행 시 10000회 이하의 연산

r_wind = []
for i in range(R):
    if chart[i][0] == -1:
        r_wind.append(i)
        chart[i][0] = 0

r_wind.sort()
l_wind = [0, R - 1]

# T초 동안 반복
for _ in range(T):
    next_chart = [[0] * C for _ in range(R)]
    # diffusion
    for i in range(R):
        for j in range(C):
            if chart[i][j]:
                loss = 0    # loss_direction
                if i + 1 < R and not (i + 1 == r_wind[0] and j == 0):
                    next_chart[i + 1][j] += chart[i][j] // 5
                    loss += chart[i][j] // 5
                if i - 1 >= 0 and not (i - 1 == r_wind[1] and j == 0):
                    next_chart[i - 1][j] += chart[i][j] // 5
                    loss += chart[i][j] // 5
                if j + 1 < C:
                    next_chart[i][j + 1] += chart[i][j] // 5
                    loss += chart[i][j] // 5
                if j - 1 >= 0 and not (j == 1 and (i in r_wind)):
                    next_chart[i][j - 1] += chart[i][j] // 5
                    loss += chart[i][j] // 5

                next_chart[i][j] += chart[i][j] - loss

    # cleaning
    for i in range(r_wind[0] - 1, -1, -1):  # 위에서 아래로(1열)
        next_chart[i + 1][0] += next_chart[i][0]
        next_chart[i][0] = 0

    for i in range(r_wind[1] + 1, R):   # 아래에서 위로(1열)
        next_chart[i - 1][0] += next_chart[i][0]
        next_chart[i][0] = 0

    next_chart[r_wind[0]][0] = 0
    next_chart[r_wind[1]][0] = 0   # 빨아들이기

    for i in l_wind:  # 좌향으로 한 칸씩 이동
        for j in range(1, C):
            next_chart[i][j - 1] += next_chart[i][j]
            next_chart[i][j] = 0

    for i in range(1, r_wind[0] + 1):   # 아래에서 위로(C - 1열)
        next_chart[i - 1][C - 1] += next_chart[i][C - 1]
        next_chart[i][C - 1] = 0

    for i in range(R - 2,  r_wind[1] - 1, -1):       # 위에서 아래로(C - 1열)
        next_chart[i + 1][C - 1] += next_chart[i][C - 1]
        next_chart[i][C - 1] = 0

    for i in r_wind:    # 우향으로 한 칸씩 이동
        for j in range(C - 2, -1, -1):
            next_chart[i][j + 1] += next_chart[i][j]
            next_chart[i][j] = 0

    for i in range(R):
        for j in range(C):
            chart[i][j] = next_chart[i][j]

res = 0
for i in range(R):
    for j in range(C):
        res += chart[i][j]

print(res)
