def get_case(x):
    if x == N - 1:
        print(path)
        path_t = [1] + path + [1]
        total = 0
        for i in range(N):
            total += arr[path_t[i] - 1][path_t[i + 1] - 1]

        sum_list.append(total)
        return
    for i in range(2, N + 1):
        if i in path: continue
        path.append(i)
        get_case(x + 1)
        path.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    path = []
    sum_list = []
    get_case(0)

    res = min(sum_list)
    print(f'#{tc} {res}')
