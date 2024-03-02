from collections import deque


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def move(y, x, dy, dx):
    cnt = 0
    while board[y + dy][x + dx] != '#':
        if board[y + dy][x + dx] == '0':
            return 0, 0, 0
        
        x += dx
        y += dy
        cnt += 1
    
    return y, x, cnt


N, M = map(int, input().split())
board = [input() for _ in range(N)]
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if board[i][j] == 'B':
            blue = [i, j]
        
        if board[i][j] == 'R':
            red = [i, j]


# bfs로 풀이
visited = {}
ry, rx, by, bx = red[0], red[1], blue[0], blue[1]
visited[ry, rx, by, bx] = 0
queue = deque([red + blue])
res = -1

while queue:
    ry, rx, by, bx = queue.popleft()
    for i in range(4):      # 네 방향으로 움직여 보면서
        nry, nrx, r = move(ry, rx, di[i], dj[i])
        nby, nbx, b = move(by, bx, di[i], dj[i])

        if not nby and not nbx:
            continue        # 파란 공이 빠진 경우 계속 탐색을 위해 continue

        elif not nry and not nrx:       # 빨간 공이 빠지면 종료
            res = visited[ry, rx, by, bx] + 1
            queue.clear()
            break

        elif nby == nry and nbx == nrx:
            if r > b:   # r이 더 많이 이동했을 경우
                nry -= di[i]
                nrx -= dj[i]
            
            else:       # b가 더 많이 이동했을 경우
                nby -= di[i]
                nbx -= dj[i]

        if (nry, nrx, nby, nbx) not in visited:     # 움직인 횟수 저장
            visited[nry, nrx, nby, nbx] = visited[ry, rx, by, bx] + 1
            queue.append([nry, nrx, nby, nbx])

        if visited[ry, rx, by, bx] >= 10:       # 10번 이상 움직였으면 실격
            queue.clear()
            break

print(res)