def solution():
    N, K = map(int, input().split())

    dp = [-1] * 100001
    # 시작점 기준 양방향 으로 DP를 채운다
    dp[N] = 0
    for i in range(N - 1, -1, -1):
        dp[i] = dp[i + 1] + 1
    for i in range(N, 100001):
        if dp[i] == -1:
            dp[i] = dp[i - 1] + 1

        if i <= 50000:
            dp[2*i] = dp[i] + 1


if __name__ == '__main__':
    solution()
