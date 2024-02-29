import sys
input = sys.stdin.readline

N = int(input())
plane = [[0] * 1001 for _ in range(1001)]
x, y, w, h = [0] * (N + 1), [0] * (N + 1), [0] * (N + 1), [0] * (N + 1)
min_x = 1001
min_y = 1001
max_x = 0
max_y = 0

for n in range(1, N + 1):
    x[n], y[n], w[n], h[n] = map(int, input().split())
    for i in range(x[n], x[n] + w[n]):
        for j in range(y[n], y[n] + h[n]):
            plane[j][i] = n

    if x[n] < min_x:
        min_x = x[n]
    if y[n] < min_y:
        min_y = y[n]
    if x[n] + w[n] > max_x:
        max_x = x[n] + w[n]
    if y[n] + h[n] > max_y:
        max_y = y[n] + h[n]

count = [0] * (N + 1)

for i in range(min_x, max_x):
    for j in range(min_y, max_y):
        if plane[j][i]:
            count[plane[j][i]] += 1

for i in range(1, N + 1):
    print(count[i])
