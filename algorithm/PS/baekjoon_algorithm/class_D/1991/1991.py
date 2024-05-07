N = int(input())
graph = [[0, 0] for _ in range(27)]   # graph express the alphabet with same idx
for i in range(1, N + 1):
    idx, son1, son2 = input().split()
    if ord(son1.lower()) - 96 > 0:
        graph[ord(idx.lower()) - 96][0] = ord(son1.lower()) - 96
    if ord(son2.lower()) - 96 > 0:
        graph[ord(idx.lower()) - 96][1] = ord(son2.lower()) - 96

# 숫자로 그래프에 저장됨
# 이를 3가지 방법으로 순회화면서 숫자를 다시 아스키코드로 변환해서 출력하면 됨
# 너무 복습을 안하니까 트리의 순회 이름도 까먹어서 찾아봐야 했다. 복습해버릇하자.


def preorder(pos):
    print(chr(pos + 96).upper(), end="")
    if graph[pos][0]:
        preorder(graph[pos][0])
    if graph[pos][1]:
        preorder(graph[pos][1])


def inorder(pos):
    if graph[pos][0]:
        inorder(graph[pos][0])

    print(chr(pos + 96).upper(), end="")

    if graph[pos][1]:
        inorder(graph[pos][1])


def postorder(pos):
    if graph[pos][0]:
        postorder(graph[pos][0])
    if graph[pos][1]:
        postorder(graph[pos][1])

    print(chr(pos + 96).upper(), end="")


preorder(1)
print()
inorder(1)
print()
postorder(1)