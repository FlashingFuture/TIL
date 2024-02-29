dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def labyrinth_search(arr):

    start = [0, 0]
    for i in range(100):
        for j in range(100):
            if arr[i][j] == '2':
                start = [i, j]

    stack = [start]
    visited = [[0] * 100 for __ in range(100)]

    while stack:         # 미로 찾기
        y, x = stack.pop()
        visited[y][x] = 1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < 100 and 0 <= nx < 100 and not visited[ny][nx]:
                if arr[ny][nx] == '0':
                    stack.append([ny, nx])
                elif arr[ny][nx] == '3':
                    return 1

    return 0
            


for _ in range(10):
    tc = int(input())

    laby = [input() for __ in range(100)]
    
    res = labyrinth_search(laby)
    print(f'#{tc} {res}')