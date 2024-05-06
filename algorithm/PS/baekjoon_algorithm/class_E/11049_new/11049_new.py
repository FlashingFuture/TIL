N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
arr = [a for a, _ in matrix] + [matrix[-1][1]]
# DP 로 푼다면
# N x N DP 를 만들어서
# 각 idx 의 행렬 연산 후의 값을 DP 에 저장하면서 이동
# 이 때 연산 가능한 경우만 연산해야 제대로 행렬 연산이 될 것
# 이후 마지막 DP를 순회해 정답을 구하면 될듯?
DP = [[0] * N for _ in range(N)]
for i in range(1, N):
    for j in range(N - i):      # 해당 위치에서 끝 위치까지 찾기
        end = i + j
        multiple_size = arr[j] * arr[end + 1]
        DP[end][j] = DP[j][end] = min(y + x + z * multiple_size for y, x, z in zip(DP[j][j:end],
                                                                                   DP[end][j + 1:end + 1],
                                                                                   arr[j + 1:end + 1]))

print(DP[0][-1])
