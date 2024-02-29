T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    amount_list = []
    for i in range(N - M + 1):
        amount = 0
        for j in range(M):
            for k in range(M):
                amount += arr[j][i + k]

        amount_list.append(amount)
        for j in range(N - M):
            for k in range(M):
                amount -= arr[j][i + k]
                amount += arr[j + M][i + k]

            amount_list.append(amount)

    res = max(amount_list)
    print(f'#{tc} {res}')