T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 1사분면만 구해볼까요
    res = 0
    for i in range(1, N):
        for j in range(1, N):
            if (i**2) + (j**2) <= N**2:
                res += 1
    res *= 4            # 4개의 사분면
    res += 4*N + 1     # x축, y축 위의 점
    print(f'#{tc} {res}')