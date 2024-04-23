import sys


MAX_ORDERS = 100000
orders = list(map(int, sys.stdin.readline().split()))
# 중앙에서 다른지점: 2
# 반대편 지점: 4
# 90도 회전 지점: 3
# 같은 지점 : 1


def movement(last, now):
    if last == 0:
        return 2
    elif abs(now - last) == 2:
        return 4
    elif now == last:
        return 1
    else:
        return 3


# 발이 두개므로 각 경우에 대해 양 발의 움직임에 대해 최솟값을 DP 로 풀이하면 될듯
# 이 경우 양 발 움직임에 따른 최솟값을 DP에 저장해가면서 해당 명령의 실행이 끝날때마다 양발의 위치 갱신
dp = [[sys.maxsize] * 5 for _ in range(5)]
# 첫 dp의 위치는 중앙(0)이므로 0만 0으로 초기화
dp[0][0] = 0
dp_next = [[sys.maxsize] * 5 for _ in range(5)]
# 0: 중앙, 1: 위, 2: 왼, 3: 아래, 4: 오른
# 어차피 같은 자리의 경우 그대로 누르는 게 dp 에 최소로 저장되므로 두 발이 겹칠 일은 없음
# orders 의 마지막은 0이므로 빼줌
orders.pop()
for new in orders:
    # 왼발(dp의 y축) 움직임
    for x in range(5):     # 이전 x 위치는 유지됨
        for y in range(5):
            power = movement(y, new)    # 이동에 드는 힘
            dp_next[new][x] = min(dp_next[new][x], dp[y][x] + power)

    # 오른발(dp의 x축) 움직임
    for y in range(5):     # 이전 y 위치 유지
        for x in range(5):
            power = movement(x, new)
            dp_next[y][new] = min(dp_next[y][new], dp[y][x] + power)

    # 해당 순회가 끝났다면 dp 를 dp_next 와 같게 갱신
    dp = [[dp_next[y][x] for y in range(5)] for x in range(5)]
    # 그 후 dp_next 는 다시 다음 값을 받도록 maxsize 로 갱신
    dp_next = [[sys.maxsize] * 5 for _ in range(5)]


res = sys.maxsize
if not orders:  # order 가 없었을 경우
    res = 0

for i in range(5):
    res = min(res, dp[orders[-1]][i])
    res = min(res, dp[i][orders[-1]])

print(res)
