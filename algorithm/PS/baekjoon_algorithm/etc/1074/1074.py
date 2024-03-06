def z_search(n, y, x):
    if n == 1:
        global cnt
        if y == r and x == c:
            print(cnt)
            return
        cnt += 1
        if y == r and x + 1 == c:
            print(cnt)
            return
        cnt += 1
        if y + 1 == r and x == c:
            print(cnt)
            return
        cnt += 1
        if y + 1 == r and x + 1 == c:
            print(cnt)
            return

        cnt += 1
        return

    else:
        n -= 1
        z_search(n, y, x)
        z_search(n, y, x + 2**n)
        z_search(n, y + 2**n, x)
        z_search(n, y + 2**n, x + 2**n)


def z_dp(n, y, x):
    for i in range(N):




N, r, c = map(int, input().split())
cnt = 0
z_search(N, 0, 0)
