T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    result = 0  # 들어갈 수 있는 자리의 개수
    for i in range(N):
        cnt_row = 0  # 연속해서 1이 나온 횟수를 저장할 카운터
        cnt_column = 0  # 세로용
        for j in range(N):
            # 가로
            if puzzle[i][j] == 1:
                cnt_row += 1
            else:
                cnt_row = 0

            if cnt_row == K:
                if j == N - 1 or puzzle[i][j+1] == 0:
                    result += 1

            # 세로
            if puzzle[j][i] == 1:
                cnt_column += 1
            else:
                cnt_column = 0

            if cnt_column == K:
                if j == N - 1 or puzzle[j+1][i] == 0:
                    result += 1

    print(f'#{tc} {result}')
