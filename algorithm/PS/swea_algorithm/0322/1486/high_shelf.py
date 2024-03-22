def backtrack(lev, total_height):
    global min_height
    if B <= total_height:
        min_height = min(min_height, total_height)
        return

    if lev == N:
        return

    backtrack(lev + 1, total_height + H[lev])   # 쌓는다
    backtrack(lev + 1, total_height)            # 안쌓는다


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    min_height = int(1e12)
    backtrack(0, 0)
    print(f'#{tc} {min_height - B}')
