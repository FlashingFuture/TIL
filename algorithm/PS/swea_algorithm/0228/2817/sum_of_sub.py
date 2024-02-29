T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    res = 0

    for i in range(1 << N): # 모든 부분 집합에 대해
        temp_sum = 0
        for j in range(N):
            if 0b1 & (i >> j):      # 해당 부분집합의 원소라면
                temp_sum += A[j]

        if temp_sum == K:
            res += 1

    print(f'#{tc} {res}')
