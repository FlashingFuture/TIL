N = int(input())
chart = [list(map(int, input().split())) for _ in range(N)]
# 2048 게임을 진행하는 문제
# 2048 게임은 N x N에 대해 한 움직임마다
# N x (N - 1)개의 판에 대해 입력된 방향에 대해 움직임을 확인
# 최대 5번 이동시키고, 방향은 상하좌우 4개므로
# 모든 경우에 대한 백트래킹을 4^5 = 1024, N은 최대 20
# 따라서 백트래킹으로 위와 같이 풀이 시
# 1024 * 400 * (이동이 되는가 / 합쳐지는가 등의 로직) 정도로 여유있을 것
# 로직이 길어진다면 가지치기에 유의하며 풀이


def movement(dy, dx):   # 입력된 방향으로 판을 움직이는 함수
    # 이동 방향의 끝점부터 합쳐지는 것이 로직이기에 dy, dx에 따라 for문이 달라짐
    if dy == - 1 and dx == 0:   # 상향
        for y in range(1, N):
            for x in range(N):
                if chart[y][x] == chart[y - 1][x]:
    return

