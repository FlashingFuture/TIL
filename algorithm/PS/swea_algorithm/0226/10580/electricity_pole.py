TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    A, B = [0] * N, [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    res = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if (A[i] < A[j] and B[i] > B[j]) or (A[i] > A[j] and B[i] < B[j]):
                res += 1

    print(f'#{tc} {res}')
