dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    pang_list = []
    for i in range(N):
        for j in range(M):
            pang_cnt = 0
            pang_cnt += arr[i][j]
            for k in range(4):
                di = dy[k]
                dj = dx[k]
                move_cnt = arr[i][j]
                while 0 <= i + di < N and 0 <= j + dj < M and move_cnt:
                    pang_cnt += arr[i + di][j + dj]
                    di += dy[k]
                    dj += dx[k]
                    move_cnt -= 1

            pang_list.append(pang_cnt)

    res = max(pang_list)
    print(f'#{tc} {res}')
