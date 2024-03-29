import sys


N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
for i in range(M):
    s, e = map(int, sys.stdin.readline().split())
    temp_list = nums[s - 1: e]
    print(sum(temp_list))
