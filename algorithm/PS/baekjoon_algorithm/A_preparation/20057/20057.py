def movement_x(y, x, dx):
    global out
    a = 0        # a의 양 계산
    if x + dx == -1:
        return
    # 출발 위치의 x축
    if 0 <= y - 1:
        chart[y - 1][x] += chart[y][x + dx] // 100
        a += chart[y][x + dx] // 100
    else:
        out += chart[y][x + dx] // 100
        a += chart[y][x + dx] // 100

    if y + 1 < N:
        chart[y + 1][x] += chart[y][x + dx] // 100
        a += chart[y][x + dx] // 100
    else:
        out += chart[y][x + dx] // 100
        a += chart[y][x + dx] // 100

    # 도착 위치의 x축
    if 0 <= x + dx < N:
        if 0 <= y - 1:
            chart[y - 1][x + dx] += chart[y][x + dx] * 7 // 100
            a += chart[y][x + dx] * 7 // 100
        else:
            out += chart[y][x + dx] * 7 // 100
            a += chart[y][x + dx] * 7 // 100

        if 0 <= y - 2:
            chart[y - 2][x + dx] += chart[y][x + dx] * 2 // 100
            a += chart[y][x + dx] * 2 // 100
        else:
            out += chart[y][x + dx] * 2 // 100
            a += chart[y][x + dx] * 2 // 100

        if y + 1 < N:
            chart[y + 1][x + dx] += chart[y][x + dx] * 7 // 100
            a += chart[y][x + dx] * 7 // 100
        else:
            out += chart[y][x + dx] * 7 // 100
            a += chart[y][x + dx] * 7 // 100

        if y + 2 < N:
            chart[y + 2][x + dx] += chart[y][x + dx] * 2 // 100
            a += chart[y][x + dx] * 2 // 100
        else:
            out += chart[y][x + dx] * 2 // 100
            a += chart[y][x + dx] * 2 // 100

    # 가장 멀리 간 축
    if 0 <= x + 3*dx < N:
        chart[y][x + 3*dx] += chart[y][x + dx] // 20
        a += chart[y][x + dx] // 20
    else:
        out += chart[y][x + dx] // 20
        a += chart[y][x + dx] // 20
    # a의 x축
    if 0 <= x + 2*dx < N:
        if 0 <= y - 1:
            chart[y - 1][x + 2*dx] += chart[y][x + dx] // 10
            a += chart[y][x + dx] // 10
        else:
            out += chart[y][x + dx] // 10
            a += chart[y][x + dx] // 10

        if y + 1 < N:
            chart[y + 1][x + 2*dx] += chart[y][x + dx] // 10
            a += chart[y][x + dx] // 10
        else:
            out += chart[y][x + dx] // 10
            a += chart[y][x + dx] // 10

        chart[y][x + dx] -= a
        chart[y][x + 2*dx] += chart[y][x + dx]
        chart[y][x + dx] = 0
    else:
        chart[y][x + dx] -= a
        out += chart[y][x + dx]
        chart[y][x + dx] = 0


def movement_y(y, x, dy):
    global out
    a = 0       # a의 남은 양을 계산할 수
    # 출발 위치의 x축
    if 0 <= x - 1:
        chart[y][x - 1] += chart[y + dy][x] // 100
        a += chart[y + dy][x] // 100
    else:
        out += chart[y + dy][x] // 100
        a += chart[y + dy][x] // 100

    if x + 1 < N:
        chart[y][x + 1] += chart[y + dy][x] // 100
        a += chart[y + dy][x] // 100
    else:
        out += chart[y + dy][x] // 100
        a += chart[y + dy][x] // 100

    # 도착 위치의 x축
    if 0 <= y + dy < N:
        if 0 <= x - 1:
            chart[y + dy][x - 1] += chart[y + dy][x] * 7 // 100
            a += chart[y + dy][x] * 7 // 100
        else:
            out += chart[y + dy][x] * 7 // 100
            a += chart[y + dy][x] * 7 // 100

        if 0 <= x - 2:
            chart[y + dy][x - 2] += chart[y + dy][x] * 2 // 100
            a += chart[y + dy][x] * 2 // 100
        else:
            out += chart[y + dy][x] * 2 // 100
            a += chart[y + dy][x] * 2 // 100

        if x + 1 < N:
            chart[y + dy][x + 1] += chart[y + dy][x] * 7 // 100
            a += chart[y + dy][x] * 7 // 100
        else:
            out += chart[y + dy][x] * 7 // 100
            a += chart[y + dy][x] * 7 // 100

        if x + 2 < N:
            chart[y + dy][x + 2] += chart[y + dy][x] * 2 // 100
            a += chart[y + dy][x] * 2 // 100
        else:
            out += chart[y + dy][x] * 2 // 100
            a += chart[y + dy][x] * 2 // 100

    # 가장 멀리 간 축
    if 0 <= y + 3*dy < N:
        chart[y + 3*dy][x] += chart[y + dy][x] // 20
        a += chart[y + dy][x] // 20
    else:
        out += chart[y + dy][x] // 20
        a += chart[y + dy][x] // 20
    # a의 x축
    if 0 <= y + 2*dy < N:
        if 0 <= x - 1:
            chart[y + 2*dy][x - 1] += chart[y + dy][x] // 10
            a += chart[y + dy][x] // 10
        else:
            out += chart[y + dy][x] // 10
            a += chart[y + dy][x] // 10

        if x + 1 < N:
            chart[y + 2*dy][x + 1] += chart[y + dy][x] // 10
            a += chart[y + dy][x] // 10
        else:
            out += chart[y + dy][x] // 10
            a += chart[y + dy][x] // 10

        chart[y + dy][x] -= a
        chart[y + 2*dy][x] += chart[y + dy][x]
        chart[y + dy][x] = 0
    else:
        chart[y + dy][x] -= a
        out += chart[y + dy][x]
        chart[y + dy][x] = 0


N = int(input())
chart = [list(map(int, input().split())) for _ in range(N)]
# 시간제한 : 1초, N <= 499 :
# 완전 탐색 시 500*500 = 250000번 순회로 시간 초과가 날 가능성은 매우 낮음
# 한 칸 움직일 때마다 chart 총 11칸의 값을 바꿔야 함
# dp가 아닌 완탐 시에도 2750000번으로 충분할 것으로 보임
out = 0
pos_y, pos_x = N // 2, N // 2    # 시작점은 중앙
# 계산의 편의성을 위해 우선 좌측 한 번 이동
movement_x(pos_y, pos_x, -1)
pos_x -= 1
m = 2   # movement
while m <= N:
    # m - 1칸 하향이동
    for i in range(m - 1):
        movement_y(pos_y, pos_x, 1)
        pos_y += 1
    # m칸 우향이동
    for i in range(m):
        movement_x(pos_y, pos_x, 1)
        pos_x += 1
    # m칸 상향이동
    for i in range(m):
        movement_y(pos_y, pos_x, -1)
        pos_y -= 1
    # m + 1칸 좌향이동
    for i in range(m + 1):
        movement_x(pos_y, pos_x, -1)
        pos_x -= 1

    m += 2

print(out)
