# 1: 1 / 2: 3 / 3: 5 / 4: 11
# dp[n] = dp[n-1] + 2*dp[n-2]
# swea에서 봤던 문제의 진화형
n = int(input())
dp = [0] * 1002
dp[0] = 0
dp[1] = 1
dp[2] = 3
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + 2*dp[i - 2]

res = dp[n]
print(res % 10007)