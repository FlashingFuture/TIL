import sys


def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    root_x, root_y = find(x), find(y)
    if root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y


G = int(sys.stdin.readline())
P = int(sys.stdin.readline())
g = [int(sys.stdin.readline()) for _ in range(P)]
# P는 최대 10^5 = 100000
# G는 최대 10^6 = 1000000
# 분리 집합을 활용하여 풀이할 수 있을 것
# 모든 비행기는 자신보다 작은 비행기에 저장할 수 있으므로
# 부모를 찾아가면서 작은 비행기를 찾아 넣어주고
# 이미 있다면 1까지 찾아가고, 1도 있다면 0을 찾아가면서 break
parents = [x for x in range(G + 1)]
count = 0
for plane in g:
    plane = find(plane)
    if plane == 0:      # 찾아 올라가도 도킹 가능한 게이트가 없다면 0
        break
    union(plane - 1, plane)     # 위치를 찾아 plane 에 저장했으니, 그 다음 게이트를 부모로 올림
    count += 1

print(count)

