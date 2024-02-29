T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    se = [list(map(int, input().split())) for _ in range(N)]
    # 종료 시간을 기준으로 정렬
    se.sort(key=lambda x: x[1])
    pos = 0
    i = 0
    res = 0
    while pos < se[N - 1][1] and i < N:
        if pos <= se[i][0]:
            res += 1
            pos = se[i][1]

        i += 1

    print(f'#{tc} {res}')