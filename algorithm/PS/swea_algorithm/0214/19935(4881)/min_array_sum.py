def npr(i, k, s):   # (i-1)까지 탐색한 원소의 합
    global min_v
    if i == k:      # 끝까지 채운 경우
        if min_v > s:
            min_v = s
    elif s >= min_v:
        return
    else:
        for j in range(i, k):
            P[i], P[j] = P[j], P[i]
            npr(i + 1, k, s + arr[i][P[i]])
            P[i], P[j] = P[j], P[i]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = [i for i in range(N)]
    min_v = 101
    npr(0, N, 0)
    print(f'#{tc} {min_v}')