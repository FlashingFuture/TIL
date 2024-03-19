import sys


def backtrack(lev, num):
    global min_diff
    if min_diff < abs(num - N):
        return

    if lev == 6:
        min_diff = abs(num - N)
        return

    for i in digit:
        if lev == 5 and no_zero and i == 0: continue
        path[lev] = i
        backtrack(lev + 1, num + i * (10 ** (5 - lev)))
        path[lev] = 0


N = int(input())
M = int(input())
if M == 0:
    B = []
else:
    B = list(map(int, input().split()))

no_zero = False
if 0 in B:
    B.remove(0)
    no_zero = True
digit = [x for x in range(10) if x not in B]
# 백트래킹으로 가장 가까운 수에 대해 접근
# 그 후 +, -버튼만으로 목표 숫자에 접근
# 그 후 그냥 +, -만 눌러서 간 값과 대소비교하여 결과 출력
path = [0] * 6
min_diff = sys.maxsize
backtrack(0, 0)
res = min(min_diff + len(str(N)), abs(N - 100))
print(res)
