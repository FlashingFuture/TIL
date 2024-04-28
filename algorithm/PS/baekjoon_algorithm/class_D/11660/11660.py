import sys      # 10만개 이상의 입력이 주어지기에 sys.stdin.readline() 사용


N, M = map(int, sys.stdin.readline().split())
chart = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# m <= 100,000, n <= 1024
# chart 를 탐색하면서 진행 시 시간초과가 날 것
# 0, 0으로부터 해당 위치까지의 직사각형의 합 dp를 만들면 될 듯하다
# dp 에는 (0, 0) 부터 해당 위치까지의 직사각형의 합 저장
# 문제에서 인덱스에 1씩 더해져서 주어지기 때문에 dp도 실제 인덱스보다 y, x가 1씩 크게 작성
dp = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + chart[i - 1][j - 1]

for m in range(M):      # m개의 케이스에 대해
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    # dp에 저장된 것은 사각형의 합이므로
    # (0, 0) 부터 (x2, y2) 까지의 큰 사각형을 잡고
    # 작은 사각형 셋(혹은 둘)을 빼서 구한다고 이해하면 될 듯
    # 이해가 안간다면 직접 그려보면서 생각해보자
    res = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
    # 아래 부분은 경계조건을 잘못 보고 설정한 처음 코드(이해하기는 더 쉬움)
    # if x1 > 0:
    #     res -= dp[y2][x1 - 1]
    # if y1 > 0:
    #     res -= dp[y1 - 1][x2]
    # if x1 > 0 and y1 > 0:       # 둘 다 빼줬다면 겹쳐서 빼준 부분을 더해줌
    #     res += dp[y1 - 1][x1 - 1]

    print(res)
