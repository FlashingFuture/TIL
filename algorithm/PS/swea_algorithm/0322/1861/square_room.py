# bfs 시간복잡도 : Node(N^2)개, EDGE(4*N^2)개로 최대 5,000,000
# 이를 N*N의 모든 위치에 다 실행한다면 최대 5,000,000,000,000회로 시간초과
# 따라서 다음 방의 value 가 +1인 경우만 탐색하는 가지치기(백트래킹)
# 해당 경우의 탐색 개수 worst case: 뱀 모양으로 정렬된 경우
# 총 bfs 횟수는 1 + 2 + ... + N**2 == N**2 * (N**2 - 1) / 2
# => 최대 500,000회로 충분히 1초 안에 27개를 돌릴 수 있음
from collections import deque


def bfs(start_y, start_x):          # 구조적으론 dfs와 동일하게 됨(문제 조건으로 인해)
    queue = deque([(start_y, start_x)])
    cnt = 0
    while queue:
        y, x = queue.popleft()
        current_value = A[y][x]
        cnt += 1
        for dy, dx in (1, 0), (-1, 0), (0, 1), (0, - 1):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if current_value + 1 == A[ny][nx]:  # value가 1 더 높은 경우만 append
                    queue.append((ny, nx))

    return [A[start_y][start_x], cnt]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    res_list = []
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            res_room, res_cnt = bfs(i, j)
            if max_cnt <= res_cnt:      # 최대카운터 이상의 값만 받아 sort의 시간복잡도를 줄임
                max_cnt = res_cnt
                res_list.append([res_room, res_cnt])
    # 먼저 방 번호를 내림차순으로 정렬하고, 그 뒤 카운트 기준 오름차순 정렬을 통해
    # res_list의 맨 뒤에 가장 카운트가 큰 값 중 가장 반 번호가 작은 값이 위치함
    res_list.sort(key=lambda x: x[0], reverse=True)
    res_list.sort(key=lambda x: x[1])

    print(f'#{tc}', end=' ')
    print(*res_list[-1])
