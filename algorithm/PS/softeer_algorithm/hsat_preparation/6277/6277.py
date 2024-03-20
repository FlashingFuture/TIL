import sys


def backtrack(lev, l, r, d, u):     # left right down up
    global min_extent
    if lev == K + 1:
        min_extent = (r - l) * (u - d)
        return

    for item in chart[lev]:
        cl = min(l, item[0])
        cr = max(r, item[0])
        cd = min(d, item[1])
        cu = max(u, item[1])
        if (cr - cl) * (cu - cd) < min_extent:
            backtrack(lev + 1, cl, cr, cd, cu)


N, K = map(int, sys.stdin.readline().split())
chart = [[] for _ in range(K + 1)]

for i in range(N):
    x, y, k = map(int, sys.stdin.readline().split())
    chart[k].append([x, y])

min_extent = 4000000

for i in range(len(chart[1])):
    x, y = chart[1][i]
    backtrack(1, x, x, y, y)

print(min_extent)
