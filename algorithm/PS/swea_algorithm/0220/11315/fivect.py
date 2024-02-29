def check_five(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                if N - i > 4:       # 가로 체크
                    for k in range(1, 5):
                        if arr[i+k][j] != 'o':
                            break

                    else:       # for k
                        return 'YES'

                if N - j > 4:       # 세로 체크
                    for k in range(1, 5):
                        if arr[i][j + k] != 'o':
                            break

                    else:       # for k
                        return 'YES'

                if N - i > 4 and N - j > 4:     # 우하향 대각선 체크
                    for k in range(1, 5):
                        if arr[i + k][j + k] != 'o':
                            break

                    else:       # for k
                        return 'YES'

                if i >= 4 and N - j > 4:        # 좌하향 대각선 체크
                    for k in range(1, 5):
                        if arr[i - k][j + k] != 'o':
                            break

                    else:       # for k
                        return 'YES'

    return 'NO'


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    plate = [input() for _ in range(N)]
    res = check_five(plate)
    print(f'#{tc} {res}')