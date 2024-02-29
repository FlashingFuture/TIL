def inorder(t):         # tree 번호가 index보다 1씩 크기에 1씩 빼줌
    if len(tree[int(t) - 1]) > 2:
        inorder(tree[int(t) - 1][2])
    word.append(tree[int(t) - 1][1])
    if len(tree[int(t) - 1]) > 3:
        inorder(tree[int(t) - 1][3])


for tc in range(1, 11):
    N = int(input())
    tree = [[] for _ in range(N)]
    for i in range(N):
        s = (input().split())
        tree[i] = s

    # tree[0]: 번호 tree[1]: 요소 tree[2]~ : 트리의 자식 노드들
    word = []
    inorder(tree[0][0])
    print(f'#{tc} {"".join(word)}')
