# 2차원 union find 를 해서
# 전체 집합의 개수를 구하면 될듯
# union find로 찾을 시 1000x1000에서 너무 길어지나?
# 시간을 줄이기 위해 dfs를 넣어야 할 것 같다(dfs 하기 싫어서 union find로 접근했는데..)
# dfs를 하는 김에 union find는 날려버리자(쓸데없다.)
import sys
sys.setrecursionlimit(2**20)


def dfs(y, x, visit_count):
    visited[y][x] = visit_count
    if direction[y][x] == 'D' and y + 1 < N:
        if not visited[y + 1][x]:
            dfs(y + 1, x, visit_count)
    elif direction[y][x] == 'L' and x - 1 >= 0:
        if not visited[y][x - 1]:
            dfs(y, x- 1, visit_count)
    elif direction[y][x] == 'U' and y - 1 >= 0:
        if not visited[y - 1][x]:
            dfs(y - 1, x, visit_count)
    elif direction[y][x] == 'R' and x + 1 < M:
        if not visited[y][x + 1]:
            dfs(y, x + 1, visit_count)
    # 주변 4점에서 여기로 오는지도 테스트해야 한다
    if y + 1 < N and direction[y + 1][x] == 'U':
        if not visited[y + 1][x]:
            dfs(y + 1, x, visit_count)
    if x - 1 >= 0 and direction[y][x - 1] == 'R':
        if not visited[y][x - 1]:
            dfs(y, x - 1, visit_count)
    if y - 1 >= 0 and direction[y - 1][x] == 'D':
        if not visited[y - 1][x]:
            dfs(y - 1, x, visit_count)
    if x + 1 < M and direction[y][x + 1] == 'L':
        if not visited[y][x + 1]:
            dfs(y, x + 1, visit_count)


N, M = map(int, sys.stdin.readline().split())
direction = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
parents = [[(i, j) for j in range(M)] for i in range(N)]
visited = [[0] * M for _ in range(N)]
res_count = 1
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(i, j, res_count)
            res_count += 1

print(res_count - 1)
