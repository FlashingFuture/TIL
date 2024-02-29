T = int(input())
for tc in range(T):         # T만큼 테스트 반복
    V, E = map(int, input().split())
    arr = [[] for _ in range(V + 1)]
    for i in range(E):
        N, M = map(int, input().split())
        arr[N].append(M)

    S, G = map(int, input().split())

    stack = []
    visited = [0] * (V + 1)
    visited[S] = 1
    while True:
        for i in arr[S]:
            if visited[i] == 0:
                stack.append(i)
                S = i
                visited[i] = 1
                break

        else:       # for i
            if stack:
                S = stack.pop()
            else:
                break   # while True

    if visited[G] == 1:
        print(f'#{tc + 1} {1}')
    else:
        print(f'#{tc + 1} {0}')
