# 3 <= N <= 8
# 1 <= K <= 5
# 모든 높이는 1 이상 20 이하의 정수
# 대충 최대 길이 64짜리를 완전탐색한다고 쳐도 굉장히 여유로움
# 모든 방향을 dfs 로 탐사
# 막히는 경우 깎을 수 있다면 깎고 탐사 지속
path = []


def backtrack(lev, y, x, h, k):      # k : 깎았는가(0), 아직 안깎았는가(1)
    global max_length
    max_length = max(max_length, lev)
    for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < N:
            if h > chart[ny][nx] and (ny, nx) not in path:
                path.append((ny, nx))
                backtrack(lev + 1, ny, nx, chart[ny][nx], k)
                path.pop()
            elif k == 1 and h > chart[ny][nx] - K and (ny, nx) not in path:
                for c_h in range(chart[ny][nx] - h + 1, K + 1):
                    path.append((ny, nx))
                    backtrack(lev + 1, ny, nx, chart[ny][nx] - c_h, 0)
                    path.pop()


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    chart = [list(map(int, input().split())) for _ in range(N)]
    max_length = 0
    start = []
    max_num = 0
    for i in range(N):  # 시작점 찾기
        for j in range(N):
            if chart[i][j] > max_num:
                max_num = chart[i][j]
                start = [(i, j)]
            elif chart[i][j] == max_num:
                start.append((i, j))

    for start_y, start_x in start:
        path.append((start_y, start_x))
        backtrack(1, start_y, start_x, max_num, 1)
        path.pop()

    print(f'#{tc} {max_length}')
