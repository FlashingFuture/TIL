import sys
from collections import deque


N, M = map(int, input().split())
graph = [sys.stdin.readline() for _ in range(N)]
# 전체 크기 1,000,000 이므로
# bfs 하면 당연히 시간 초과 아님?
# 빈 공간 마다 그 빈 공간에 닿은 모든 벽에 그 빈 공간의 크기만큼 더해줌
# 그러면 모든 빈 공간에 대해 빈 공간의 크기를 구하고 그 테두리에 그 크기만큼 더해주면 될 것
# 1. 빈 공간들을 각각의 구역으로 나눔
# 각 구역을 한 점에 할당하는 방식으로 진행
empty_square_graph = [[int(graph[n][m]) for m in range(M)] for n in range(N)]
for i in range(N):
    for j in range(M):
        if empty_square_graph[i][j] == 0:
            total_area = 1
            queue = deque([(i, j)])
            empty_square_graph[i][j] = -1
            while queue:
                y, x = queue.popleft()
                for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < M and empty_square_graph[ny][nx] == 0:
                        total_area += 1
                        queue.append((ny, nx))
                        empty_square_graph[ny][nx] = -1

            empty_square_graph[i][j] = total_area

print(empty_square_graph)
result_graph = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if empty_square_graph[i][j] >= 1:
            if graph[i][j] == 1:
                result_graph[i][j] += 1
            else:
                area_size = empty_square_graph[i][j]
                queue = deque([(i, j)])
                while queue:
                    y, x = queue.popleft()
                    empty_square_graph[i][j] = -2
                    for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < M:
                            if empty_square_graph[ny][nx] == -1:
                                queue.append((ny, nx))
                            elif empty_square_graph[ny][nx] == 1:
                                result_graph[ny][nx] = result_graph[ny][nx] + area_size

print(result_graph)
