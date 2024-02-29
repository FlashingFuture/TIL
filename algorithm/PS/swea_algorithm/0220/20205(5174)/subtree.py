def preorder(t):        # preorder로 트리를 순회하면서 subtree의 크기를 구함
    global cnt
    cnt += 1
    if tree[t - 1]:
        for item in tree[t - 1]:
            preorder(item)


T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    tree = [[] for _ in range(E + 1)]
    arr = list(map(int, input().split()))
    for i in range(E):
        tree[arr[2*i] - 1].append(arr[2*i + 1])

    cnt = 0
    preorder(N)
    print(f'#{tc} {cnt}')