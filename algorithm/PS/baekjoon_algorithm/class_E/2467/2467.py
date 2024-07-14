import sys


N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
# N <= 100000
# 투 포인터를 이용해 탐색하면 20만번 x a(a < 10)만 찾으면 되는거 아님?
min_diff = 100000000001
i = 0
j = N - 1
answer = [0, N - 1]
while i < j:
    value = arr[i] + arr[j]
    if abs(value) < min_diff:
        min_diff = abs(value)
        answer = [arr[i], arr[j]]
    # 우선 음수가 더해질 때까지 최대한 j를 내려봄
    if value > 0:
        j -= 1
    else:
        i += 1


print(*answer)
