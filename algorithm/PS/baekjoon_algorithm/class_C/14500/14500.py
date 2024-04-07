objects = [
    [[0, 0], [0, 1], [0, 2], [0, 3]],   # right 3
    [[0, 0], [1, 0], [2, 0], [3, 0]],   # down 3
    [[0, 0], [0, 1], [1, 0], [1, 1]],   # square
    # 2번후 꺾이는 도형
    [[0, 0], [0, 1], [0, 2], [1, 2]],   # right 2
    [[0, 0], [1, 0], [2, 0], [2, 1]],   # r down 2
    [[0, 0], [0, 1], [1, 1], [2, 1]],   # right 1
    [[0, 0], [1, 0], [1, 1], [1, 2]],   # r down 1
    [[1, 0], [0, 0], [0, 1], [0, 2]],   # left 1
    [[2, 0], [1, 0], [0, 0], [0, 1]],   # left 2
    [[2, 0], [2, 1], [1, 1], [0, 1]],   # l down 1
    [[1, 0], [1, 1], [1, 2], [0, 2]],   # l down 2

    # s자 도형
    [[0, 0], [0, 1], [1, 1], [1, 2]],   # r d r
    [[0, 0], [1, 0], [1, 1], [2, 1]],   # d r d
    [[1, 0], [1, 1], [0, 1], [0, 2]],   # d l d
    [[0, 1], [1, 1], [1, 0], [2, 0]],   # r u r
    # 볼록할철
    [[0, 0], [0, 1], [0, 2], [1, 1]],
    [[0, 0], [1, 0], [2, 0], [1, 1]],
    [[1, 0], [1, 1], [1, 2], [0, 1]],
    [[0, 1], [1, 1], [2, 1], [1, 0]],
]


N, M = map(int, input().split())
chart = [list(map(int, input().split())) for _ in range(N)]
# 그냥 구현이야 임마
max_num = 0
for i in range(N):
    for j in range(M):
        max_temp = 0
        for item in objects:
            temp = 0
            for pos in item:
                if i + pos[0] < N and j + pos[1] < M:
                    temp += chart[i + pos[0]][j + pos[1]]

            max_temp = max(temp, max_temp)

        max_num = max(max_num, max_temp)

print(max_num)
