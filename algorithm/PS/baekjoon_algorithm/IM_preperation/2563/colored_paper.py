N = int(input())

plane = [[0] * 100 for _ in range(100)]
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            plane[x + i][y + j] = 1

res = 0
for i in range(100):
    for j in range(100):
        if plane[i][j] == 1:
            res += 1

print(res)