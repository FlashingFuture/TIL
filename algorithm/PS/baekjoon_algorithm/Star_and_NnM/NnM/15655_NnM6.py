import sys
# 심신이 안정되는 N과 M
picked_number = []


def backtrack(lev, start):
    if lev == M:
        print(*picked_number)
        return

    for idx in range(start, N):
        picked_number.append(arr[idx])
        backtrack(lev + 1, idx + 1)
        picked_number.pop()


N, M = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

backtrack(0, 0)
