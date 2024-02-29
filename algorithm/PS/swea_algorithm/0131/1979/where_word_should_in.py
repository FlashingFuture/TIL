T = int(input()) # count of test case
for t in range(1, T + 1): # T만큼 테스트 반복
    N, K = map(int, input().split())
    arr = []
    for i in range(N):
        line = list(map(int, input().split()))
        arr.append(line)

    position_fit = 0 # 딱 칸이 맞는 경우를 셀 변수
    for i in range(N):
        # 딱 N개만큼 1이 연속적으로 있고, 그 앞뒤에는 0이 있는 경우
        for j in range(1, N - K):
            column_sum = 0
            row_sum = 0
            for k in range(K):
                column_sum += arr[i][j + k]
                row_sum += arr[j + k][i]

            if column_sum == K:
                if arr[i][j - 1] == arr[i][j + K] == 0:
                    position_fit += 1
            if row_sum == K:
                if arr[j - 1][i] == arr[j + K][i] == 0:
                    position_fit += 1

    for i in range(N):
        # 시작 / 끝이 배열의 끝에 닿아 있는 경우
        column_sum_left = 0
        column_sum_right = 0
        row_sum_high = 0
        row_sum_low = 0
        for k in range(K):
            column_sum_left += arr[i][k]
            column_sum_right += arr[i][N - k - 1]
            row_sum_high += arr[k][i]
            row_sum_low += arr[N - k - 1][i]

        if column_sum_left == K and arr[i][K] == 0:
            position_fit += 1
        if column_sum_right == K and arr[i][N - K - 1] == 0:
            position_fit += 1
        if row_sum_high == K and arr[K][i] == 0:
            position_fit += 1
        if row_sum_low == K and arr[N - K - 1][i] == 0:
            position_fit += 1

    print(f'#{t} {position_fit}')