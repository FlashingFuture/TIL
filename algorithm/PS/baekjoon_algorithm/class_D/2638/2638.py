# N, M <= 100
# 한 번 전체 공간에 대해 완전탐색를 하면 최대 100 * 4
# 이 때 2칸 이상 0에 닿은 모든 칸에 대해 dfs / bfs 를 하여 정답을 구하면
# 2500000번 이하로 계산을 끝내야함
# 잘 찾기만 하면 될듯?
import sys


N, M = map(int, sys.stdin.readline().split())
chart = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 치즈가 녹는 경우를 대비해 다음 치즈들의 위치를 저장하면서 갈 chart 필요
new_chart = [[chart[i][j] for j in range(M)] for i in range(N)]


def melt_check(start_y, start_x):
    # 가장자리까지 가면 공기에 노출된 것이므로 dfs 가 유리(사실 bfs 도 되긴 할듯)
    stack = [(start_y, start_x)]
    visited = [[chart[i][j] for j in range(M)] for i in range(N)]
    while stack:
        y, x = stack.pop()
        for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
            ny, nx = y + dy, x + dx
            if ny <= 0 or ny >= N - 1 or nx <= 0 or nx >= M - 1:
                return 1     # 바깥에 닿았다면 return 1
            elif not visited[ny][nx]:
                stack.append((ny, nx))
                visited[ny][nx] = 1

    return 0        # 바깥에 닿지 못했다면 return 0


time_count = 0
while True:     # chart 의 치즈가 전부 녹을 때까지
    is_cheese_left = False
    for i in range(N):          # 치즈가 남아있는지 확인
        for j in range(M):
            if new_chart[i][j]:
                is_cheese_left = True

    if not is_cheese_left:
        break           # 치즈가 남지 않았다면 break

    for i in range(N):      # 전체 chart 순회
        for j in range(M):
            if chart[i][j]:     # 치즈가 있다면
                air_count = 0
                for di, dk in (1, 0), (-1, 0), (0, 1), (0, -1):
                    ni, nj = i + di, j + dk
                    if 0 <= ni < N and 0 <= nj < M and not chart[ni][nj]:
                        air_count += melt_check(ni, nj)  # 바깥 공기라면 count += 1

                if air_count >= 2:
                    new_chart[i][j] = 0

    time_count += 1  # 시간을 1 올려줌

    # chart 순회가 끝난 후, new_chart 의 값을 chart 에 넣어줌
    chart = [[new_chart[i][j] for j in range(M)] for i in range(N)]

print(time_count)
