di = [1, 0, -1, 0, 1, 1, -1, -1]  # 상하좌우, 대각4방향
dj = [0, 1, 0, -1, 1, -1, 1, -1]  # 상하좌우, 대각4방향

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())    # N : 판의 크기,  M : 돌을 놓는 횟수

    plate = [[0] * N for _ in range(N)]
    plate[(N-1)//2][(N-1)//2], plate[(N+1)//2][(N+1)//2] = 2, 2     # 시작 흰돌
    plate[(N-1)//2][(N+1)//2], plate[(N+1)//2][(N-1)//2] = 1, 1     # 시작 흑돌

    # 돌을 놓으면 해당 지점부터
    # 반대 색깔 돌로 차 있는 모든 방향으로 나아가
    # 같은 색깔을 만날때까지 이동하여
    # 만나면 지나온 경로를 전부 같은 색깔로 변경
    for _ in range(M):
        y, x, color = map(int, input().split())
        plate[y - 1][x - 1] = color

        for k in range(8):
            stack = []
            i = y - 1
            j = x - 1
            while True:
                i += di[k]
                j += dj[k]
                if 0 > i or 0 > j or N <= i or N <= j or plate[i][j] == 0:
                    stack = []
                    break
                elif color == plate[i][j]:
                    break

                stack.append([i, j])

            while stack:
                temp = stack.pop()
                plate[temp[0]][temp[1]] = color

    count_black = 0
    count_white = 0
    for i in range(N):
        for j in range(N):
            if plate[i][j] == 1:
                count_black += 1
            elif plate[i][j] == 2:
                count_white += 1

    print(f'#{tc} {count_black} {count_white}')
