# 방법 1
# 0.1초 : 최대 천만 번 연산?

char1 = ' ' + input().rstrip()
char2 = ' ' + input().rstrip()
N = len(char1)
M = len(char2)
dp = [[0] * M for _ in range(N)]
for i in range(1, N):
    for j in range(1, M):
        if char1[i] == char2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

res = dp[-1][-1]
print(res)