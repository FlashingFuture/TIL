T = int(input())
for tc in range(1, T + 1):  # 테스트 케이스 수만큼 반복
    N = int(input())    # 달팽이의 크기
    # N만큼 오른쪽으로 감 -> N-1만큼 아래 / 왼쪽으로 ->
    # N-2만큼 위 / 오른쪽 ...
    arr = [[0]*N for _ in range(N)]
    temp = 1   # 1씩 늘어나는 배열 저장값을 넣어줄 변수
    for i in range(N // 2):
        for j in range(N - 2 * i - 1):  # move right
            arr[i][j + i] = temp
            temp += 1
        for j in range(N - 2 * i - 1):  # move down
            arr[j + i][N - i - 1] = temp
            temp += 1
        for j in range(N - 2 * i - 1):  # move left
            arr[N - i - 1][N - i - 1 - j] = temp
            temp += 1
        for j in range(N - 2 * i - 1):  # move up
            arr[N - i - 1 - j][i] = temp
            temp += 1

    if N % 2 == 1:
        arr[N // 2][N // 2] = temp

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')

        print()