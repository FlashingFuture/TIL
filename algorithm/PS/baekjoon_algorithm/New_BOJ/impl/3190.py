# https://www.acmicpc.net/problem/3190


from collections import deque


def init():
    n = int(input())
    k = int(input())
    apples = [list(map(int, input().split())) for _ in range(k)]
    l = int(input())
    movement = []
    for _ in range(l):
        time, direction = input().split()
        movement.append((int(time), direction))

    # 사과를 기반으로 게임판 생성
    board = [[0] * n for _ in range(n)]
    for y, x in apples:
        board[y - 1][x - 1] = 1

    return n, board, movement


def get_end_time(n, board, movement):
    body = deque([(0, 0)])
    dy, dx = 0, 1
    time_count = 0
    movement_idx = 0
    while True:
        time_count += 1
        ny, nx = body[0][0] + dy, body[0][1] + dx
        if ny < 0 or ny >= n or nx < 0 or nx >= n or (ny, nx) in body:
            return time_count

        elif board[ny][nx] == 1:
            board[ny][nx] = 0
            body.appendleft((ny, nx))

        else:
            body.appendleft((ny, nx))
            body.pop()

        if movement_idx < len(movement) and time_count == movement[movement_idx][0]:
            dy, dx = get_new_direction(dy, dx, movement[movement_idx][1])
            movement_idx += 1


def get_new_direction(dy, dx, turn):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    idx = directions.index((dy, dx))
    if turn == 'L':
        idx = (idx - 1) % 4
    elif turn == 'D':
        idx = (idx + 1) % 4

    return directions[idx]


if __name__ == "__main__":
    n, board, movement = init()
    print(get_end_time(n, board, movement))