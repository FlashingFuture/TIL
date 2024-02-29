T = int(input())
for tc in range(1, T + 1):
    D, A, B, F = map(int, input().split())
    total_dist = D * F / (A + B)
    print(f'#{tc} {total_dist}')


