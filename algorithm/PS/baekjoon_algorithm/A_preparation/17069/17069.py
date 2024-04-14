N = int(input())
chart = [list(map(int, input().split())) for _ in range(N)]
# 누가봐도 dp
# 아래를 못감 / 위를 못감 을 잡아줘야 함
dp = [[[0] * 3 for _ in range(N)] for __ in range(N)]
# dp[][][0]: 이전 값이 대각선, 1: 이전 값이 가로, 2: 이전 값이 세로
for i in range(1, N):
    if chart[0][i]:
        break
    dp[0][i][1] = 1     # 맨 윗줄은 가로이동만으로 초기화

# (0, 1)부터 출발하여 dp로 탐색하면서 이동
for i in range(1, N):
    for j in range(1, N):
        if not chart[i][j]:     # 현위치가 막혀있지 않다면
            dp[i][j][1] = dp[i][j-1][0] + dp[i][j-1][1]     # 가로 이동
            dp[i][j][2] = dp[i-1][j][0] + dp[i-1][j][2]     # 세로 이동
            if not chart[i][j-1] and not chart[i-1][j]:     # 대각선 4칸이 비면
                dp[i][j][0] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

res = sum(dp[N-1][N-1])
print(res)