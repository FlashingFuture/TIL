import sys


def solution():
    N = int(input())
    W = [list(map(int, input().split())) for _ in range(N)]
    # N 의 크기는 최대 16이므로
    # N x (2^N) 배열을 선언한 후(크기 약 2백만)
    # 비트마스킹을 활용한 DP를 사용하면 될 듯
    dp = [[sys.maxsize] * N for _ in range(1 << N)]
    # 0번 도시에서 시작
    dp[1][0] = 0

    for visited in range(1 << N):
        for last_city in range(N):
            if visited & (1 << last_city):
                for next_city in range(N):
                    if visited & (1 << next_city) == 0 and W[last_city][next_city] != 0:
                        dp[visited | (1 << next_city)][next_city] \
                            = min(dp[visited | (1 << next_city)][next_city],
                                  dp[visited][last_city] + W[last_city][next_city])

    result = sys.maxsize
    for i in range(1, N):
        if W[i][0] != 0:
            result = min(result, dp[(1 << N) - 1][i] + W[i][0])

    print(result)


if __name__ == "__main__":
    solution()
