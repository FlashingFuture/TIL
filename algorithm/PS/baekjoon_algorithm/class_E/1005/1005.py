import sys
from collections import deque


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    # 요구조건 건물 X 와 이후 건설가능 건물 Y 를 그래프로 둠
    # 그래프 안의 값을 리스트로 구성해 필요조건을 저장
    graph = [[0, []] for _ in range(N + 1)]
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        graph[X][1].append(Y)
        graph[Y][0] += 1

    W = int(input())
    # 각 위치에서 시작하여 탐색하면서 DP로 풀이하면 될듯?
    DP = [0 for _ in range(N + 1)]
    queue = deque([])
    # 큐 초기화 : 아무 조건 없이 지을 수 있는 건물들 건설
    for i in range(1, N + 1):
        if graph[i][0] == 0:
            queue.append(i)
            DP[i] = D[i - 1]

    while queue:    # 조건에 맞춰 탐색 가능 건물들을 늘리면서 BFS
        pos = queue.popleft()
        for next_pos in graph[pos][1]:
            graph[next_pos][0] -= 1
            DP[next_pos] = max(DP[next_pos], DP[pos] + D[next_pos - 1])
            if graph[next_pos][0] == 0:
                queue.append(next_pos)

    print(DP[W])