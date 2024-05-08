import sys


N = int(input())
graph = [[] for _ in range(N + 1)]
# 루트를 1로 잡을 것이므로 양방향으로 graph 에 노드를 저장함
for _ in range(N - 1):
    parent, child = map(int, sys.stdin.readline().split())
    graph[parent].append(child)
    graph[child].append(parent)

# 트리를 탐색하되 부모 노드에서 자식 노드 값에 접근하면서 탐색해 출력하기
# 처음으로 찾으면 끝내야 하므로 dfs 가 유리
# 100000x100000(100억) 이라 일일히 dfs 하면 시간초과가 날것?
# visited 를 dp로 활용하여 딱 한번만 dfs 돌리자


def dfs(start):
    stack = [start]
    visited = [0] * (N + 1)
    visited[1] = 1
    while stack:
        pos = stack.pop()
        if graph[pos]:       # 트리에 원소(자식)가 있다면
            for child_pos in graph[pos]:
                if not visited[child_pos]:
                    stack.append(child_pos)
                    visited[child_pos] = pos

    for i in range(2, N + 1):
        print(visited[i])


dfs(1)
