from collections import deque


N, M = map(int, input().split())
island = [list(map(int, input().split())) for _ in range(N)]
# 풀이 1번
# 우선 섬의 개수를 구한 후
# 섬이 전부 이어지는 경우를 전부 구한 후
# 그 중 가장 짧은 경우를 찾는다?
# 그렇다면 각 섬은 visited에 주는 숫자를 각각 다르게 하여 확인
visited = [[0] * M for _ in range(N)]


def bfs(y_input, x_input, n):
    queue = deque([(y_input, x_input)])
    visited[y_input][x_input] = n
    while queue:
        y, x = queue.popleft()
        for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and island[ny][nx] == 1:
                visited[ny][nx] = n
                queue.append((ny, nx))


num = 1
island_start = []
for i in range(N):
    for j in range(M):
        if island[i][j] == 1 and not visited[i][j]:
            island_start.append((i, j))
            bfs(i, j, num)
            num += 1

for i in range(N):
    print(visited[i])

# 이제 섬이 이어지는 경우의 수를 전부 확인
# 이는 각 섬마다의 최단거리를 구하면 쉽게 확인가능(이어지지 못할 경우 -1)


def bfs_distance(y_input, x_input):
    queue = deque([(y_input, x_input)])
    n = visited[y_input][x_input]
    visited[y_input][x_input] = 7
    while queue:
        y, x = queue.popleft()
        for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] == n:
                    queue.append((ny, nx))
                    visited[ny][nx] = 7    # 섬은 최대 6개기에 7로 초기화

                elif visited[ny][nx] == 0:
                    while 0 <= ny < N and 0 <= nx < M:
                        ny, nx = ny + dy, nx + dx
                        if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 7:
                            continue
                        elif 0 <= ny < N and 0 <= nx < M and visited[ny][nx]:
                            delta = max(abs(ny - y), abs(nx - x)) - 1
                            if delta > 1:
                                connections.append((n, visited[ny][nx], delta))
                            break


connections = []
for item in island_start:
    bfs_distance(item[0], item[1])


connections = list(set(connections))
print(connections)
# connections 최대의 원소 개수는 5 + 4 + 3 + 2 + 1 = 15
# 이제 연결만 잘 해서 최솟값만 구하면 됨
# 풀이 1 : bfs를 통해 하나씩 연결해 가면서 연결된 모든 경우를 구해 그 중 최솟값을 구하기
# 이를 위해 트리 형태로 연결값들을 재구성
tree = [[] for _ in range(len(island_start) + 1)]

for item in connections:
    tree[item[0]].append([item[1], item[2]])
    tree[item[1]].append([item[0], item[2]])

print(tree)
# tree 탐색 실행
ans_list = []
path = [1, ]


def backtrack(n, total):

    if len(path) == len(island_start):
        ans_list.append(total)
        return

    if len(tree) > n:
        for k in range(len(tree[n])):
            if tree[n][k][0] in path: continue
            path.append(tree[n][k][0])
            backtrack(tree[n][k][0], total + tree[n][k][1])
            path.pop()


backtrack(1, 0)

print(ans_list)
