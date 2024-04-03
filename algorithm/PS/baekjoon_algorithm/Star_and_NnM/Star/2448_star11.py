triangle_delta = [
    (-1, 0), (0, 1), (0, -1), (1, -2),
    (1, -1), (1, 0), (1, 1), (1, 2)
]

N = int(input())
chart = [[' '] * (2*N - 1) for _ in range(N)]
# 삼각형은 재귀적으로 2배씩 커지는 구조
# N = 6일 때 삼각형 높이 12, 삼각형 밑변의 길이 12
# 내부에 밑변 5짜리 삼각형 3개로 이루어진 구조
# 중앙점을 기준으로 위로 두칸, 왼쪽으로 세칸 후 아래로 한 칸, 오른쪽으로도 같음
# N = 6 삼각형부터 구현
# 시작점은 N = 6일 때 y = 4, N = 12일 때 y = 8과 같이 3*x 에 대해 2*x


def triangle(y, x):
    for dy, dx in triangle_delta:
        chart[y + dy][x + dx] = '*'


def recur(y, x, n):
    if n == 1:
        triangle(y, x)
        return

    n //= 2
    recur(y - 2 * n, x, n)
    recur(y + n, x + 3 * n, n)
    recur(y + n, x - 3 * n, n)


P = N // 3
recur(2 * P - 1, 3 * P - 1, P)
for line in chart:
    print(''.join(line))
