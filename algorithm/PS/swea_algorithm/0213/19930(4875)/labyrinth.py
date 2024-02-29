di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def labyrinth_search(arr, n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '2':
                start = [i, j]

    stack = [start]      # 노드들을 저장할 스택
    visited = [[0] * n for _ in range(n)]
    visited[start[0]][start[1]] = 1
    while stack:        # 스택이 완전히 빌 때까지
        y, x = stack.pop()
        visited[y][x] = 1
        for i in range(4):
            ny = y + di[i]
            nx = x + dj[i]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if arr[ny][nx] == '3':
                    return 1
                elif arr[ny][nx] == '0':
                    stack.append([ny, nx])

    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    char = [input() for _ in range(N)]
    res = labyrinth_search(char, N)
    print(f'#{tc} {res}')
