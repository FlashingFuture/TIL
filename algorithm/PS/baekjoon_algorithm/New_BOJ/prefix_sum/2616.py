# https://www.acmicpc.net/problem/2616


import sys


def solution():
    n = int(input())
    trains = list(map(int, sys.stdin.readline().split()))
    max_train = int(input())
    prefix_sum = [0]
    value = 0
    for train in trains:
        value += train
        prefix_sum.append(value)

    dp = [[0] * 4 for _ in range(n + 1)]

    for train in range(1, 4):
        for i in range(max_train * train, n + 1):
            if train == 1:
                dp[i][train] = max(dp[i - 1][train], prefix_sum[i] - prefix_sum[i - max_train])

            else:
                dp[i][train] = max(dp[i - 1][train], dp[i - max_train][train - 1] + prefix_sum[i] - prefix_sum[i - max_train])


    print(dp[n][3])

solution()