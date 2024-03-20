import sys


N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
for i in range(M):
    s, e = map(int, sys.stdin.readline().split())
    temp = 0
    for k in range(s - 1, e):
        temp += nums[k]
    print(temp)
