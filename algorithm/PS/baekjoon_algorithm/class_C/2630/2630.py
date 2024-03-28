N = int(input())
chart = [list(map(int, input().split())) for _ in range(N)]


def binary_cut(y, x, n):
    blue_cnt = 0
    white_cnt = 0
    global blue_res
    global white_res
    for i in range(y, y + n):
        for j in range(x, x + n):
            if chart[i][j] == 0:
                white_cnt += 1
            else:
                blue_cnt += 1

            if blue_cnt and white_cnt:
                n //= 2
                binary_cut(y, x, n)
                binary_cut(y, x + n, n)
                binary_cut(y + n, x, n)
                binary_cut(y + n, x + n, n)
                return

    if blue_cnt:
        blue_res += 1
    else:
        white_res += 1
    return


blue_res, white_res = 0, 0
binary_cut(0, 0, N)
print(white_res)
print(blue_res)
