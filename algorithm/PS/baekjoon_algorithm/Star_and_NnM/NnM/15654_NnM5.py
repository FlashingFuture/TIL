from itertools import permutations


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
combs = permutations(nums, M)
res_list = list(combs)
for item in res_list:
    print(*item)