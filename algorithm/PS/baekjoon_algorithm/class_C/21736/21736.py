import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
chart = [sys.stdin.readline() for _ in range(N)]
# 간단한 BFS 1회 문제, BFS 시간복잡도 : 600*600 == 360000 으로 충분함
# (while문 하나에서 1200회 이하로만 연산하면 됨)
# -> while 내 for문 하나에서 대략 300회 이하로 연산하면 충분함
visited = [[0] * M for _ in range(N)]
queue = deque([])
for i in range(N):
    for j in range(M):
        if chart[i][j] == 'P':
            visited[i][j] = -1      # 사람이 있는 곳은 -1로 초기화
        elif chart[i][j] == 'X':
            visited[i][j] = 1       # 벽은 못가야하기에 방문처리
        elif chart[i][j] == 'I':
            queue.append((i, j))

met_personnel = 0
while queue:
    y, x = queue.popleft()
    for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] <= 0:
            queue.append((ny, nx))
            if visited[ny][nx] == -1:
                met_personnel += 1
            visited[ny][nx] = 1

if met_personnel == 0:
    met_personnel = 'TT'
print(met_personnel)
