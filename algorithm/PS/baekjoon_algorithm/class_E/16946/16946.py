import sys
from collections import deque

N, M = map(int, input().split())
graph = [sys.stdin.readline() for _ in range(N)]

# 전체 크기 1,000,000 이므로 BFS
# 빈 공간 마다 그 빈 공간에 닿은 모든 벽에 그 빈 공간의 크기만큼 더해줌
# 그러면 모든 빈 공간에 대해 빈 공간의 크기를 구하고 그 테두리에 그 크기만큼 더해주면 될 것

# 빈 공간에 대한 정보
empty_square_graph = [[-1] * M for _ in range(N)]  # 각 칸의 구역 ID
area_sizes = []  # 각 구역의 크기 저장


def bfs_area(y, x, area_id):
    queue = deque([(y, x)])
    empty_square_graph[y][x] = area_id
    size = 1
    while queue:
        cy, cx = queue.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == '0' and empty_square_graph[ny][nx] == -1:
                empty_square_graph[ny][nx] = area_id
                size += 1
                queue.append((ny, nx))
    return size


area_id = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == '0' and empty_square_graph[i][j] == -1:
            area_size = bfs_area(i, j, area_id)
            area_sizes.append(area_size)
            area_id += 1

# 결과 그래프 초기화
result_graph = [[0] * M for _ in range(N)]

# 벽을 부수고 이동할 수 있는 칸 계산
for i in range(N):
    for j in range(M):
        if graph[i][j] == '1':
            # 인접한 구역들의 크기를 합산
            adjacent_areas = set()
            for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + dy, j + dx
                if 0 <= ni < N and 0 <= nj < M and graph[ni][nj] == '0':
                    area_id = empty_square_graph[ni][nj]
                    adjacent_areas.add(area_id)

            total_size = 1  # 현재 벽 포함
            for area_id in adjacent_areas:
                total_size += area_sizes[area_id]

            result_graph[i][j] = total_size % 10

# 결과 출력
for i in range(N):
    for j in range(M):
        if graph[i][j] == '0':
            print(0, end='')
        else:
            print(result_graph[i][j], end='')
    print()
