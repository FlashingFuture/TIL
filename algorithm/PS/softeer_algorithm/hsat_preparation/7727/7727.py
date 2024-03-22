# 시간복잡도
# 한 점이 4개짜리 경로를 만드는 모든 경우 : 64
# 3개의 경로 수 : 2^24 = 16777216
#
import sys


def backtrack(p_lev, lev, y, x):
    if lev == 3:
        if p_lev == m:
            global max_num
            temp_sum = 0
            for fy in range(n):
                for fx in range(n):
                    if visited[fy][fx]:
                        temp_sum += chart[fy][fx]

            max_num = max(max_num, temp_sum)
            return

        next_y, next_x = friends[p_lev][0] - 1, friends[p_lev][1] - 1
        backtrack(p_lev + 1, 0, next_y, next_x)
        return

    for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < n:
            visited[ny][nx] += 1
            backtrack(p_lev, lev + 1, ny, nx)
            visited[ny][nx] -= 1


n, m = map(int, sys.stdin.readline().split())
chart = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
friends = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

visited = [[0] * n for _ in range(n)]
max_num = 0
for item in friends:
    visited[item[0] - 1][item[1] - 1] = 1

backtrack(1, 0, friends[0][0] - 1, friends[0][1] - 1)
print(max_num)
