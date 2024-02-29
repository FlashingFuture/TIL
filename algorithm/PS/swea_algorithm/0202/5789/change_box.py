T = int(input())
for tc in range(1, T + 1):
    N, Q = map(int, input().split())    # 상자의 개수 N, 작업횟수 Q
    arr = [0] * N
    for i in range(1, Q + 1):
        L, R = map(int, input().split())    # 작업할 범위 L, R
        for j in range(L - 1, R):
            arr[j] = i      # L~R의 상자에 i값을 넣음

    print(f'#{tc} {" ".join(map(str, arr))}')
