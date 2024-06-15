from collections import deque


T = int(input())
for tc in range(T):
    L = int(input())
    start_y, start_x = map(int, input().split())
    end_y, end_x = map(int, input().split())
    visited = [[0] * (L + 1) for _ in range(L + 1)]
    queue = deque([(start_y, start_x)])
    visited[start_y][start_x] = 1
    while queue:
        y, x = queue.popleft()
        if (y, x) == (end_y, end_x):
            print(visited[y][x] - 1)
            break

        for dy, dx in (1, 2), (2, 1), (2, -1), (1, -2), (-1, 2), (-2, 1), (-2, -1), (-1, -2):
            ny, nx = y + dy, x + dx
            if 0 <= ny < L and 0 <= nx < L and not visited[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1
