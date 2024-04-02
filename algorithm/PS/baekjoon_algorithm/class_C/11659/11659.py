import sys


N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
sum_list = []
temp = 0
for i in range(N):
    temp += nums[i]
    sum_list.append(temp)

for i in range(M):
    s, e = map(int, sys.stdin.readline().split())
    res = sum_list[e - 1] - sum_list[s - 1] + nums[s - 1]
    print(res)
