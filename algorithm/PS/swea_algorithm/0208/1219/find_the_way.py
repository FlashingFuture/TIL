def dfs(graph):
    stack = []               # DFS를 실행할 스택
    visited = [0] * 100  # DFS 방문 기록을 저장할 리스트
    point = 0
    visited[point] = 1       # 문제 조건에 맞춰 0부터 탐색
    while True:
        for j in graph[point]:
            if visited[j] == 0:
                stack.append(j)
                point = j
                visited[j] = 1
                break

        else:   # for j
            if stack:
                point = stack.pop()
            else:
                break   # while True

    if visited[99] == 1:
        return 1
    else:
        return 0


while True:
    try:
        N, M = map(int, input().split())
    except EOFError:
        break

    arr = list(map(int, input().split()))
    near_list = [[] for _ in range(100)]

    for i in range(M):
        near_list[arr[2*i]].append(arr[2*i + 1])

    ans = dfs(near_list)
    print(f'#{N} {ans}')


