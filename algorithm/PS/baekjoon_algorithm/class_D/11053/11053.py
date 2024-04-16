N = int(input())
A = list(map(int, input().split()))
# DP인 거 같긴 한데
# 시간복잡도는 1000x999/2 < 500000으로 매우 여유있음
DP = [1] * N    # 수열과 같은 크기의 DP 배열 선언

for i in range(1, N):
    for j in range(i - 1, -1, -1):
        if A[i] > A[j] and DP[i] <= DP[j]:    # A[i]의 크기가 더 크고, 수열 길이가 최대일 때
            DP[i] = DP[j] + 1

res = max(DP)
print(res)
