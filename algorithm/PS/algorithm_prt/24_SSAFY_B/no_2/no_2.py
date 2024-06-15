T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    mask = (1 << N) - 1
    ans = "ON" if (M & mask) == mask else 'OFF'
    print(f'#{tc} {ans}')