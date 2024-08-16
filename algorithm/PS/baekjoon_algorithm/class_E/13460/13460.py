from collections import deque


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
# N, M <= 10
# 각 경우에 대해 bfs 를 진행 (10번 조건을 체크 하기 편함)
# 각 시행 에서 R, B 만이 이동
# 함수에 R 위치, B 위치, 시행 횟수를 저장해 풀이


def find_start():
    ri, rj, bi, bj = 0, 0, 0, 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                ri, rj = i, j
                board[i][j] = '.'
            if board[i][j] == 'B':
                bi, bj = i, j

    return ri, rj, bi, bj


result = 11
Ry, Rx, By, Bx = find_start()
queue = deque([(Ry, Rx, By, Bx, 1)])
while queue:
    ry, rx, by, bx, count = queue.popleft()
    for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
        nry, nrx, nby, nbx = ry + dy, rx + dx, by + dy, bx + dx
        while 0 <= nry < N and 0 <= nrx < M and board[nry][nrx] != 'O' and board[nry][nrx] :


