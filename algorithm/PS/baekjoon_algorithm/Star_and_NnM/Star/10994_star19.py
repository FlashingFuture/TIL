def make_blank_left(n, y, x):
    arr[y][x - 1] = ' '
    n -= 1
    if n <= 0:
        return
    make_blank_left(n, y, x - 2)


def make_blank_right(n, y, x):
    arr[y][x + 1] = ' '
    n -= 1
    if n <= 0:
        return
    make_blank_right(n, y, x + 2)


def make_blank_up(n, y, x):
    arr[y - 1][x] = ' '
    n -= 1
    if n <= 0:
        return
    make_blank_up(n, y - 2, x)


def make_blank_down(n, y, x):
    arr[y + 1][x] = ' '
    n -= 1
    if n <= 0:
        return
    make_blank_down(n, y + 2, x)


def go_lu(n, y, x):
    n -= 1
    if n <= 0:
        return
    arr[y - 1][x - 1] = ' '
    make_blank_left(n, y, x)
    make_blank_left(n, y - 1, x)
    go_lu(n, y - 2, x - 2)


def go_ul(n, y, x):
    n -= 1
    if n <= 0:
        return
    make_blank_up(n, y, x)
    make_blank_up(n, y, x - 1)
    go_ul(n, y - 2, x - 2)


def go_ru(n, y, x):
    n -= 1
    if n <= 0:
        return
    arr[y - 1][x + 1] = ' '
    make_blank_right(n, y, x)
    make_blank_right(n, y - 1, x)
    go_ru(n, y - 2, x + 2)


def go_ur(n, y, x):
    n -= 1
    if n <= 0:
        return
    make_blank_up(n, y, x)
    make_blank_up(n, y, x + 1)
    go_ur(n, y - 2, x + 2)


def go_rd(n, y, x):
    n -= 1
    if n <= 0:
        return
    arr[y + 1][x + 1] = ' '
    make_blank_right(n, y, x)
    make_blank_right(n, y + 1, x)
    go_rd(n, y + 2, x + 2)


def go_dr(n, y, x):
    n -= 1
    if n <= 0:
        return
    make_blank_down(n, y, x)
    make_blank_down(n, y, x + 1)
    go_dr(n, y + 2, x + 2)


def go_ld(n, y, x):
    n -= 1
    if n <= 0:
        return
    arr[y + 1][x - 1] = ' '
    make_blank_left(n, y, x)
    make_blank_left(n, y + 1, x)
    go_ld(n, y + 2, x - 2)


def go_dl(n, y, x):
    n -= 1
    if n <= 0:
        return
    make_blank_down(n, y, x)
    make_blank_down(n, y, x - 1)
    go_dl(n, y + 2, x - 2)


N = int(input())

arr = [['*'] * (4*N - 3) for _ in range(4*N - 3)]

go_lu(N, (4*N - 3) // 2, (4*N - 3) // 2)
go_ul(N, (4*N - 3) // 2, (4*N - 3) // 2)
go_ru(N, (4*N - 3) // 2, (4*N - 3) // 2)
go_ur(N, (4*N - 3) // 2, (4*N - 3) // 2)
go_rd(N, (4*N - 3) // 2, (4*N - 3) // 2)
go_dr(N, (4*N - 3) // 2, (4*N - 3) // 2)
go_ld(N, (4*N - 3) // 2, (4*N - 3) // 2)
go_dl(N, (4*N - 3) // 2, (4*N - 3) // 2)

for a in range(4*N - 3):
    print(''.join(arr[a]))
