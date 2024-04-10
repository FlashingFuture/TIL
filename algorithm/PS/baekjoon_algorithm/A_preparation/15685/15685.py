N = int(input())
chart = [[0] * 101 for _ in range(101)]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    path = [d]
    # 0: 우향, 1: 상향, 2: 좌향, 3: 하향
    for j in range(g):
        for k in range(len(path) -1, -1, -1):
            path.append((path[k] + 1) % 4)

    chart[y][x] = 1
    for r in path:
        if r == 0:
            x += 1
        elif r == 1:
            y -= 1
        elif r == 2:
            x -= 1
        elif r == 3:
            y += 1

        chart[y][x] = 1

res = 0
for i in range(100):
    for j in range(100):
        if chart[i][j] and chart[i+1][j] and chart[i][j+1] and chart[i+1][j+1]:
            res += 1

print(res)
