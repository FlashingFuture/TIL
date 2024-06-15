N = int(input())
stairs = [int(input()) for _ in range(N)]
# DP 로 풀이
# 각 계단에서의 상태는 다음 칸을 갈 수 있음 / 다음 칸을 갈 수 없음 으로 나뉨
# 따라서 2 X 300 짜리 배열을 만들어 각각 최댓값을 저장하면서 DP 로 풀면 될 것
# 이 경우 시간복잡도는 3 x 300 = 600
# stairs 0번 index를 계산 시 1번 index처럼 사용
DP = [[0] * 2 for _ in range(N + 3)]
DP[1] = [stairs[0], stairs[0]]
if N > 1:
    DP[2][0] = stairs[1]

for i in range(1, N - 1):
    # 1칸 이동(이후 다음 칸 못감) 후 값 비교
    DP[i + 1][1] = DP[i][0] + stairs[i]
    # 2칸 이동
    DP[i + 2][0] = max(DP[i][0], DP[i][1]) + stairs[i + 1]

DP[N][1] = DP[N - 1][0] + stairs[N - 1]
print(max(DP[N]))