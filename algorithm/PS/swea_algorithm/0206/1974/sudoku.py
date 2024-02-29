T = int(input())
for tc in range(1, T + 1):      # T번만큼 테스트 반복
    arr = [list(map(int, input().split())) for _ in range(9)]   # 9x9 스도쿠
    ans = 1
    for i in range(9):
        # 가로
        count = [0] * 9  # 스도쿠 검증을 위해 사용할 크기 9짜리 1차원 배열
        for j in range(9):
            count[arr[i][j] - 1] += 1

        if max(count) != 1:
            ans = 0
            break

        # 세로
        count = [0] * 9
        for j in range(9):
            count[arr[j][i] - 1] += 1

        if max(count) != 1:
            ans = 0
            break

    # 3x3 사각형
    for i in range(3):
        for j in range(3):
            count = [0] * 9
            for k in range(3):
                for L in range(3):
                    count[arr[3 * i + k][3 * j + L] - 1] += 1

            if max(count) != 1:
                ans = 0
                break

    print(f'#{tc} {ans}')