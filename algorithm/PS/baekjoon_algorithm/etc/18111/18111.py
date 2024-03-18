import sys
input = sys.stdin.readline


N, M, B = map(int, input().split())
chart = []
for i in range(N):
    chart += list(map(int, input().split()))

max_num = max(chart)
min_num = min(chart)
res = sys.maxsize
for i in range(min_num, max_num + 1):
    blocks = B
    total_time = 0
    for j in range(N * M):
        blocks += chart[j] - i
        total_time += i - chart[j]
        if i < chart[j]:
            total_time += 3 * (chart[j] - i)
    if blocks < 0 or res < total_time:
        i -= 1
        break

    res = total_time

print(res, i)