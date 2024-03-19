def backtrack(lev, y, x):
    if lev == 7:
        case_dict[''.join(path)] = 1
        return

    for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
        ny, nx = y + dy, x + dx
        if 0 <= ny < 4 and 0 <= nx < 4:
            path.append(str(plate[ny][nx]))
            backtrack(lev + 1, ny, nx)
            path.pop()


T = int(input())
for tc in range(1, T + 1):
    plate = [list(map(int, input().split())) for _ in range(4)]
    case_dict = {}
    path = []
    for i in range(4):
        for j in range(4):
            backtrack(0, i ,j)

    res = len(case_dict)
    print(f'#{tc} {res}')
