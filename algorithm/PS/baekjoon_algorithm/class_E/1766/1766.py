import sys
from heapq import heappush, heappop


N, M = map(int, sys.stdin.readline().split())    # 문제의 수 N, 정보의 수 M
is_required = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    is_required[B].append(A)
# 우선순위 큐를 만들되
# 1. 먼저 풀면 좋은 문제가 있는지 확인
# 2. 아직 안풀었으면 대기하다 그 문제가 풀리면 우선순위 큐에 집어넣는다
# 이런 식으로 풀면 될듯?

pq = []