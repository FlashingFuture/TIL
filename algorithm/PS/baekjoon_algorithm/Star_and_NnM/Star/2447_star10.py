delta_x = [1, 1, 0, -1, -1, -1, 0, 1]
delta_y = [0, 1, 1, 1, 0, -1, -1, -1]


def make_blank(y, x, n):
    n = n // 3
    if n == 0:
        return
    else:
        for i in range(n):
            for j in range(n):
                arr[y - ((n + 1) // 2) + i][x - ((n + 1) // 2) + j] = ' '

        for i in range(8):
            make_blank(y + n * delta_y[i], x + n * delta_x[i], n)


N = int(input())

arr = [['*'] * N for _ in range(N)]

make_blank((N+1) // 2, (N+1) // 2, N)

for a in range(N):
    for b in range(N):
        print(arr[a][b], end='')
    print()
