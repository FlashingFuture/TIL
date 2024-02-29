T = int(input())
for tc in range(1, T + 1):
    A = list(range(1, 13))

    N, K = map(int, input().split())
    result = []
    for i in range(2 ** 12):    # 2^12 만큼 순회
        for j in range(12):     #
            if i & (2 ** j) == True:    # j가 i의 부분집합일 때?





