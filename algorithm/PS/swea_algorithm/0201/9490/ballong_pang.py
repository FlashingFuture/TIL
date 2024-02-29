T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 과녁 arr을 쏘아 터진 꽃가루의 개수 구하기
    max_pollen = 0 # 최대 꽃가루
    for i in range(N):
        for j in range(M):
            # 해당 과녁을 쏘았을 때의 꽃가루
            pollens = arr[i][j]
            for k in range(1, arr[i][j] + 1):
                if i - k >= 0:
                    pollens += arr[i-k][j]
                if i + k <= N - 1:
                    pollens += arr[i+k][j]
                if j - k >= 0:
                    pollens += arr[i][j-k]
                if j + k <= M - 1:
                    pollens += arr[i][j+k]

            if max_pollen < pollens:
                max_pollen = pollens

    print(f'#{tc} {max_pollen}')