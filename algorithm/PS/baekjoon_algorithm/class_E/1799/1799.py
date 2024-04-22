import sys


sys.setrecursionlimit(2**31 - 1)
N = int(input())        # 체스판의 크기
plate = [list(map(int, input().split())) for _ in range(N)]
# 백트래킹 시 최악의 경우에
# 2^100 = 10^(3 * 10)
# 다만 cannot 에 저장하는 행동이 이후 경우를 100~0회 줄여줌
# 실행시켜 보면 이 로직으로는 N=7까지만 제한시간을 만족
# 비숍은 옆에 있는 칸에는 영향을 못 주고, 대각선으로만 영향을 주기에
# 인덱스의 합이 홀수인 격자, 짝수인 격자로 분할정복해 풀이하면
# 2^50으로 바꿔 풀이할 수 있다
# 각각 cannot 배열을 만들어 못 가는 자리를 확인하면서 백트래킹
cannot = [[0] * N for _ in range(N)]


def make_cannot(y, x, disable):     # y, x에 비숍을 놓거나 뺄 때 갱신해주는 함수
    # 좌하향 대각선
    temp_y, temp_x = y, x
    while temp_y < N and temp_x >= 0:
        cannot[temp_y][temp_x] += disable
        temp_y += 1
        temp_x -= 1
    # 우하향 대각선
    temp_y, temp_x = y + 1, x + 1
    while temp_y < N and temp_x < N:
        cannot[temp_y][temp_x] += disable
        temp_y += 1
        temp_x += 1


def backtrack_even(y, x, num_of_bishop):    # (y + x)가 짝수인 판에 대한 백트래킹
    if x >= N - 2:     # 맨 오른쪽 위치일 때
        if y == N - 1:              # 마지막 줄일 때
            global max_bishop_even
            if plate[y][x] and not cannot[y][x]:
                max_bishop_even = max(max_bishop_even, num_of_bishop + 1)
            else:
                max_bishop_even = max(max_bishop_even, num_of_bishop)
            return
        else:                       # 마지막 줄이 아닌 맨 오른쪽 위치일 때
            if plate[y][x] and not cannot[y][x]:
                make_cannot(y, x, 1)
                backtrack_even(y + 1, (y + 1) % 2, num_of_bishop + 1)
                make_cannot(y, x, -1)
            backtrack_even(y + 1, (y + 1) % 2, num_of_bishop)
    else:   # 맨 오른쪽이 아닐 때
        if plate[y][x] and not cannot[y][x]:
            make_cannot(y, x, 1)
            backtrack_even(y, x + 2, num_of_bishop + 1)
            make_cannot(y, x, -1)
        backtrack_even(y, x + 2, num_of_bishop)


def backtrack_odd(y, x, num_of_bishop):     # (y + x)가 홀수인 판에 대한 백트래킹
    if x >= N - 2:     # 맨 오른쪽 위치일 때
        if y == N - 1:              # 마지막 줄일 때
            global max_bishop_odd
            if plate[y][x] and not cannot[y][x]:
                max_bishop_odd = max(max_bishop_odd, num_of_bishop + 1)
            else:
                max_bishop_odd = max(max_bishop_odd, num_of_bishop)
            return
        else:                       # 마지막 줄이 아닌 맨 오른쪽 위치일 때
            if plate[y][x] and not cannot[y][x]:
                make_cannot(y, x, 1)
                backtrack_odd(y + 1, y % 2, num_of_bishop + 1)
                make_cannot(y, x, -1)
            backtrack_odd(y + 1, y % 2, num_of_bishop)
    else:   # 맨 오른쪽이 아닐 때
        if plate[y][x] and not cannot[y][x]:
            make_cannot(y, x, 1)
            backtrack_odd(y, x + 2, num_of_bishop + 1)
            make_cannot(y, x, -1)
        backtrack_odd(y, x + 2, num_of_bishop)


if N == 1:
    print(plate[0][0])
else:
    max_bishop_even = 0
    max_bishop_odd = 0
    backtrack_even(0, 0, 0)
    backtrack_odd(0, 1, 0)
    res = max_bishop_even + max_bishop_odd
    print(res)
