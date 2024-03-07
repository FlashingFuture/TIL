from collections import deque


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

N, M = map(int, input().split())
laby = [input() for _ in range(N)]
visited = [[0] * M for _ in range(N)]

queue = deque([(0, 0)])
visited[0][0] = 1
ans_list = []
while queue:
    y, x = queue.popleft()
    for i in range(4):
        ny, nx = y + di[i], x + dj[i]
        if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0 and laby[ny][nx] == '1':
            queue.append((ny, nx))
            visited[ny][nx] = visited[y][x] + 1 
            if ny == N - 1 and nx == M - 1:
                print(visited[ny][nx])
                queue.clear()
                break

