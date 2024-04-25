import sys
from heapq import heappush, heappop


N, M = map(int, sys.stdin.readline().split())    # 문제의 수 N, 정보의 수 M
# 우선순위 큐를 만들되
# 1. 먼저 풀면 좋은 문제가 있는지 확인
# 2. 아직 안풀었으면 대기하다 그 문제가 풀리면 우선순위 큐에 집어넣는다
# 이런 식으로 풀면 될듯?
# M의 범위가 N보다 넓으므로(여러 선수문제를 지정하는 문제가 있을 수 있으므로)
# 후속 문제를 저장하는 그래프를 만들고
# 후속 문제가 전부 나왔음을 확인한 후 해당 문제를 우선순위 큐에 집어넣도록 설계
solve_after = [[] for _ in range(N + 1)]
num_of_required = [0] * (N + 1)     # 선수 문제 수를 저장할 배열
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    solve_after[A].append(B)    # 선수문제에 후순위 문제 배정
    num_of_required[B] += 1     # 선수문제의 개수 + 1

pq = []
for i in range(1, N + 1):   # 우선 선수문제가 없는 문제들만 pq에 배정
    if not num_of_required[i]:
        heappush(pq, i)

res_list = []
while pq:
    solved = heappop(pq)
    res_list.append(solved)
    for next_p in solve_after[solved]:      # 후속 문제들에 대해
        num_of_required[next_p] -= 1        # 선수문제 개수 - 1
        if not num_of_required[next_p]:     # 남은 선수문제가 없다면
            heappush(pq, next_p)            # pq에 heappush

print(*res_list)
