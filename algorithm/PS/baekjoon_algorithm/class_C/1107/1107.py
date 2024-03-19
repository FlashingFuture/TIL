import sys


def is_able(num):
    temp = str(num)
    for item in temp:
        if item in B:
            return 1000000

    return abs(num - N) + len(str(num))


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
if M == 0:
    B = []
else:
    B = list(sys.stdin.readline().split())

choose_min = 1000000
for i in range(1000001):
    cost = is_able(i)
    if cost < choose_min:
        choose_min = cost

res = min(choose_min, abs(N - 100))
print(res)
