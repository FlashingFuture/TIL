DP = [None] * 11


def dp():
    DP[0] = 0
    DP[1] = 1
    DP[2] = 2
    DP[3] = 4
    for i in range(4, 11):
        DP[i] = DP[i - 1] + DP[i - 2] + DP[i - 3]


dp()
T = int(input())
for tc in range(T):
    n = int(input())
    print(DP[n])