N = int(input())
DIV_NUM = 10 ** 9
# DP 로 풀면 될듯?
# 0, 9의 경우 커지거나 작아지지 못하는 점을 고려하여
# 10 x N DP 배열을 선언하여 풀이
DP = [[0] * 10 for _ in range(N)]
# 첫번째 수는 0인 경우는 없도록 초기화
for i in range(1, 10):
    DP[0][i] = 1

for i in range(1, N):
    DP[i][0] = DP[i - 1][1]  # 0은 이전 수가 1
    DP[i][9] = DP[i - 1][8]  # 9는 이전 수가 8
    for k in range(1, 9):   # 1부터 8까지
        DP[i][k] = DP[i - 1][k - 1] + DP[i - 1][k + 1]


res = sum(DP[N - 1]) % DIV_NUM
print(res)
