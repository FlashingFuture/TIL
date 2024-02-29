def find_way(i, j, total_sum):
    total_sum += arr[i][j]
    global min_val
    if total_sum > min_val:     # 가지치기
        return
    if i == j == (N - 1):
        min_val = total_sum
        return

    if i < N - 1:
        find_way(i + 1, j, total_sum)

    if j < N - 1:
        find_way(i, j + 1, total_sum)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_val = 999999
    find_way(0, 0, 0)
    res = min_val

    print(f'#{tc} {res}')
