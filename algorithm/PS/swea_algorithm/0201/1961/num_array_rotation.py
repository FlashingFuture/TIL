T = int(input())
for tc in range(1, T + 1):  # 테스트 케이스 T만큼 테스트
    N = int(input())    # 입력받는 숫자 배열의 크기
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))  # 배열을 입력받음

    arr_90 = [[0]*N for _ in range(N)]  # 90도 돌린 배열
    for i in range(N):
        for j in range(N):
            arr_90[i][j] = arr[N - j - 1][i]

    arr_180 = [[0]*N for _ in range(N)]  # 180도 돌린 배열
    for i in range(N):
        for j in range(N):
            arr_180[i][j] = arr_90[N - j - 1][i]  # 90도 돌린걸 또 90도 돌림

    arr_270 = [[0]*N for _ in range(N)]  # 270도 돌린 배열
    for i in range(N):
        for j in range(N):
            arr_270[i][j] = arr_180[N - j - 1][i]  # 180도 돌린걸 또 90도 돌림

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr_90[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(arr_180[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(arr_270[i][j], end='')

        print()
