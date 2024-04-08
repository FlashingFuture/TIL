from collections import deque


N = int(input())
chart = [list(map(int, input().split())) for _ in range(N)]
# 공간 최대 크기는 20x20
# 전체 탐색 한 번에 최대 400 : 400번 bfs 해도 시간은 넘침
# 아기 상어의 시작 크기는 2
stack = []
# 시작점 찾기
for i in range(N):
    for j in range(N):
        if chart[i][j] == 9:
            stack.append((i, j))

size = 2
size_cnt = 0
time_cnt = 0
while stack:
    start_y, start_x = stack.pop()
    chart[start_y][start_x] = 0
    # 각 포지션에서 bfs 를 통해 다음 위치를 찾고, 이를 스택에 넣음
    visited = [[0] * N for _ in range(N)]
    visited[start_y][start_x] = 1
    queue = deque([(start_y, start_x)])     # 시간을 위해 움직인 칸을 계산할 카운트 0 초기화
    while queue:
        temp_next_start = (N, N)
        y, x = queue.popleft()
        for dy, dx in (-1, 0), (0, -1), (0, 1), (1, 0):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and chart[ny][nx] <= size:       # 먹거나 지나갈 수 있음
                queue.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1

    next_pos = (N, N)
    min_visited = 999
    for i in range(N):
        for j in range(N):
            if 1 <= chart[i][j] < size and visited[i][j] < min_visited and visited[i][j]:
                min_visited = visited[i][j]
                next_pos = (i, j)

    if next_pos[0] != N:
        stack.append(next_pos)
        time_cnt += min_visited - 1
        size_cnt += 1
        if size_cnt == size:
            size += 1
            size_cnt = 0

print(time_cnt)
