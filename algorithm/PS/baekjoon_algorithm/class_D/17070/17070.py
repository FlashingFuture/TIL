import sys


# last_vec : 0(하향), 1(대각 우하향), 2(우향)
def backtrack(lev, last_vec, y, x):
    if lev == 2*N - 3:
        global cnt
        cnt += 1
        return

    if last_vec != 0:   # 하향인 경우 우향이 불가능
        if x < N - 1 and chart[y][x + 1] == 0:
            backtrack(lev + 1, 2, y, x + 1)

    if last_vec != 2:   # 우향인 경우 하향이 불가능
        if y < N - 1 and chart[y + 1][x] == 0:
            backtrack(lev + 1, 0, y + 1, x)

    if x < N - 1 and y < N - 1 and not chart[y + 1][x + 1] and not chart[y + 1][x] and not chart[y][x + 1]:
        backtrack(lev + 2, 1, y + 1, x + 1)


N = int(sys.stdin.readline())
chart = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt = 0
backtrack(0, 2, 0, 1)
print(cnt)
