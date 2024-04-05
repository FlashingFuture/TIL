import sys


N = int(sys.stdin.readline())
chart = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = chart[0][0]
for i in range(1, N):
    # 좌방향으로 내려가기
    for k in range(i):
        dp[i][k] = dp[i - 1][k] + chart[i][k]

    # 우방향으로 내려가되, 더 큰 경우에만 내려감
    for k in range(i):
        temp = dp[i - 1][k] + chart[i][k + 1]
        if temp > dp[i][k + 1]:
            dp[i][k + 1] = temp

res = max(dp[N - 1])
print(res)