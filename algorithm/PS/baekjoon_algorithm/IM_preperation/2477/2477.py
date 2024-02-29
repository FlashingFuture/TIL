from collections import deque


N = int(input())    # 1칸에 자라는 참외의 개수 N
# 3 1 3 1 과 같이 두 방향이 연달아 두 번씩 나온다면, 그 중 2, 3번째의 값이 실제로 빠지는 부분
L = deque([list(map(int, input().split())) for _ in range(6)])
size = 0

for _ in range(6):
    if L[0][0] == L[2][0] and L[1][0] == L[3][0]:
        size = L[4][1] * L[5][1] - L[1][1] * L[2][1]

    L.append(L.popleft())

res = size * N
print(res)
