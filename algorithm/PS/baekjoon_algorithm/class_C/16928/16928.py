from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
portal = [[0] * (N + M) for _ in range(2)]
for i in range(N + M):
    s, e = map(int, input().split())
    portal[0][i], portal[1][i] = s - 1, e - 1

queue = deque([0])
visited = [-1] * 100
visited[0] = 0
while queue:
    x = queue.popleft()
    if x == 99:
        break
    for dx in range(1, 7):
        nx = x + dx
        if nx in portal[0]:
            nx = portal[1][portal[0].index(nx)]

        if nx < 100 and visited[nx] == -1:
            queue.append(nx)
            visited[nx] = visited[x] + 1

print(visited[99])
