def inorder(t):
    global value
    if tree[t]:
        inorder(tree[t][0])
    node_value[t] = value
    value += 1
    if len(tree[t]) == 2:
        inorder(tree[t][1])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = [[] for _ in range(N + 1)]
    node_value = [0] * (N + 1)
    for i in range(1, N + 1):       # 완전 이진 트리 형태 만들기
        if 2*i < N:
            tree[i].append(2 * i)
            tree[i].append(2 * i + 1)
        elif 2*i == N:
            tree[i].append(2 * i)
        else:
            break

    value = 1
    inorder(1)
    print(f'#{tc} {node_value[1]} {node_value[N // 2]}')
