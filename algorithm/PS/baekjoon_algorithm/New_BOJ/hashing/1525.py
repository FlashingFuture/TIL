# https://www.acmicpc.net/problem/1525


from collections import deque


def init():
    puzzle = get_string_puzzle()
    visited = set([puzzle])
    print(bfs(puzzle, visited))


def get_string_puzzle():
    puzzle = ''
    for _ in range(3):
        puzzle += ''.join(input().split())
    return puzzle


def bfs(puzzle, visited):
    x_movement = [-1, 1, -3, 3]
    y_movement = [-3, 3]
    q = deque([(puzzle, 0)])


    while q:
        state, count = q.popleft()
        blank_idx = state.index('0')

        if state == "123456780":
            return count

        for dx in x_movement:
            nx = blank_idx + dx
            if dx == 1 and blank_idx in (2, 5) or (dx == -1 and blank_idx in (3, 6)):
                continue

            if 0 <= nx < 9:
                new_state = ''
                target_num = state[nx]
                target_idx = state.index(target_num)
                for i in range(9):
                    if i == blank_idx:
                        new_state += target_num
                    elif i == nx:
                        new_state += '0'
                    else:
                        new_state += state[i]

                if new_state not in visited:
                    q.append((new_state, count + 1))
                    visited.add(new_state)

    return -1


if __name__ == "__main__":
    init()