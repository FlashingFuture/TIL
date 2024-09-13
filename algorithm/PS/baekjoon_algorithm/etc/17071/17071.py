import sys
from collections import deque


N, K = map(int, input().split())

sys.setrecursionlimit(1270000000)
sister = [-1] * 500001
# 2500만번까지 가능
# 대충 동생의 위치는 최대 1000
# 그렇다면 동생이 수빈을 찾으러 갈때
# 25000번 안에만 찾으면된다?
queue = deque([(N, 0)])

while queue:


sister_move_count = 0
sister_speed = 0
sister_pos = K
while sister_pos <= 500000:
    sister[sister_pos] = sister_move_count
    sister_move_count += 1
    sister_pos += sister_move_count


fastest_count = 500001
for i in range(500001):
    print(subin[i])
    if subin[i] == sister[i]:
        fastest_count = min(fastest_count, subin_dfs[i])

    if sister[i] >= 0:
        print(sister[i], 'sis', i)
if fastest_count > 500000:
    fastest_count = -1

print(fastest_count)