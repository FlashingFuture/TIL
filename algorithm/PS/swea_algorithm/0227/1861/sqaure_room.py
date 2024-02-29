di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    max_room = 0
    res_rooms = []
    for i in range(N):
        for j in range(N):
            cnt = 1
            stack = [[i, j]]
            while stack:
                y, x = stack.pop()
                for k in range(4):
                    ni = y + di[k]
                    nj = x + dj[k]
                    if 0 <= ni < N and 0 <= nj < N and A[ni][nj] == A[y][x] + 1:
                        stack.append([ni, nj])
                        cnt += 1

            if cnt > max_room:
                res_rooms = [A[i][j]]
                max_room = cnt

            elif cnt == max_room:
                res_rooms.append(A[i][j])

    print(f'#{tc} {min(res_rooms)} {max_room}')
