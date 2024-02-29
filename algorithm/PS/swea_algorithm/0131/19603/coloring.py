T = int(input())
for t in range(1, T + 1):
    N = int(input()) # 칠할 영역의 개수 N
    color = [] # 칠할 구역을 저장
    for n in range(N):
        color.append(list(map(int, input().split())))

    red = [[0]*10 for _ in range(10)]
    blue = [[0]*10 for _ in range(10)]
    for i in range(N):
        if color[i][4] == 1: # red
            for j in range(color[i][0], color[i][2] + 1):     # y축 범위
                for k in range(color[i][1], color[i][3] + 1): # x축 범위
                    red[j][k] = 1
        if color[i][4] == 2: # blue
            for j in range(color[i][0], color[i][2] + 1):     # y축 범위
                for k in range(color[i][1], color[i][3] + 1): # x축 범위
                    blue[j][k] = 1

    # 빨강 / 파랑 둘 다 칠해지는 경우에만 purple을 올림
    purple = 0

    for i in range(10):
        for j in range(10):
            if red[i][j] == blue[i][j] == 1:
                purple += 1

    print(f'#{t} {purple}')



