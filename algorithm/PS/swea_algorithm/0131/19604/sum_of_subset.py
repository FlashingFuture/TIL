T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())

    A = list(range(1, 13))

    result = [[] for _ in range(13)]  # 원소의 개수 / 부분집합의 합을 저장할 이중리스트
    for i in range(1 << 12):  # 모든 A의 부분집합에 대해
        sum_val = 0
        cnt_val = 0
        for j in range(12):  # A의 모든 원소에 대해
            if i & (1 << j):  # 해당 원소가 부분집합에 포함될 경우
                sum_val += A[j]
                cnt_val += 1

        result[cnt_val].append(sum_val)

    print(f'#{tc} {result[N].count(K)}')