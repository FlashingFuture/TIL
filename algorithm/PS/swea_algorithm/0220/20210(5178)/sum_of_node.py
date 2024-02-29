def postorder(t):
    if tree[t]:
        postorder(tree[t][0])
        temp = node_value[tree[t][0]]
        if len(tree[t]) == 2:
            postorder(tree[t][1])
            temp += node_value[tree[t][1]]

        node_value[t] = temp


T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):       # 완전 이진 트리 형태 만들기
        if 2*i < N:
            tree[i].append(2 * i)
            tree[i].append(2 * i + 1)
        elif 2*i == N:
            tree[i].append(2 * i)
        else:
            break

    node_value = [0] * (N + 1)
    for i in range(M):
        n, x = map(int, input().split())
        node_value[n] = x

    postorder(1)
    print(f'#{tc} {node_value[L]}')
