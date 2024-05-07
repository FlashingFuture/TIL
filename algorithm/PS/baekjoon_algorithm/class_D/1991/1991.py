N = int(input())
graph = [[] * 27]   # graph express the alphabet with same idx
for i in range(1, N + 1):
    idx, son1, son2 = input().split()
    if ord(son1.lower()) - 96 > 0:
        graph[i].append(ord(son1.lower()) - 96)
    if ord(son2.lower()) - 96 > 0:
        graph[i].append(ord(son2.lower()) - 96)

# 숫자로 그래프에 저장됨
# 이를 3가지 방법으로 순회화면서 숫자를 다시 아스키코드로 변환해서 출력하면 됨


def preorder():
    return


