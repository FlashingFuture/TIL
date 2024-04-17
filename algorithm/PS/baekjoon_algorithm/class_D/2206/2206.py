import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
chart = [sys.stdin.readline() for _ in range(N)]
# 맵의 최대 크기 : 1000 X 1000
# 일반적인 bfs 실행 시 시간 복잡도는 대략 1000000 X 10(대충 while문 한번의 동작)?
# 아마도 bfs를 벽 부수기 포함해 두 번 진행해도 시간초과는 안 날 것
queue = deque([(0, 0, 0)])     # 좌표 (1, 1) = 0행 0열, 벽은 아직 안부숨
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
visited_broke = [[0] * M for _ in range(N)]
while queue:
    y, x, is_broke = queue.popleft()        # is_broke : 벽을 부쉈는가
    for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M:
            if not is_broke and not visited[ny][nx]:
                if chart[ny][nx] == '1':
                    if not visited_broke[ny][nx]:
                        queue.append((ny, nx, 1))   # 벽을 부쉈기에 is_broke는 1이 될 것
                        visited_broke[ny][nx] = visited[y][x] + 1
                else:
                    queue.append((ny, nx, 0))
                    visited[ny][nx] = visited[y][x] + 1

            elif is_broke and not visited_broke[ny][nx] and chart[ny][nx] == '0':
                queue.append((ny, nx, 1))
                visited_broke[ny][nx] = visited_broke[y][x] + 1

# visited 배열을 두 개 만들었기에 최종 결과값에 유의하기
# 하나의 값만 0이라면 0이 아닌 값을, 아니라면 둘 중 최솟값을 반환
if visited[-1][-1] == visited_broke[-1][-1] == 0:
    res = -1
elif visited[-1][-1] == 0:
    res = visited_broke[-1][-1]
elif visited_broke[-1][-1] == 0:
    res = visited[-1][-1]
else:
    res = min(visited[-1][-1], visited_broke[-1][-1])

print(res)