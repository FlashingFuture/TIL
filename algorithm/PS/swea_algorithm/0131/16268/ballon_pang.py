T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    # 과녁 arr을 쏘아 터진 꽃가루의 개수 구하기
    max_pollen = 0 # 최대 꽃가루
    for i in range(N):
        for j in range(M):
            # 해당 과녁을 쏘았을 때의 꽃가루
            pollens = arr[i][j]
            if i != 0:
                pollens += arr[i-1][j]
            if i != N - 1:
                pollens += arr[i+1][j]
            if j != 0:
                pollens += arr[i][j-1]
            if j != M - 1:
                pollens += arr[i][j+1]

            if max_pollen < pollens:
                max_pollen = pollens

    print(f'#{t} {max_pollen}')

