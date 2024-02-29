N = int(input())    # 기둥의 개수 N
L = [[0] * 2 for _ in range(N)]

for i in range(N):
    L[i][0], L[i][1] = map(int, input().split())    # L[i][0] : x, L[i][1] : height

L.sort()

y_max = 0
pos_max = 0
for i in range(N):                              # max(y) 찾기
    if y_max < L[i][1]:
        y_max = L[i][1]
        pos_max = L[i][0]

height = 0
length = 0
total_area = 0
for i in range(0, L.index([pos_max, y_max])):           # 왼쪽 끝에서 최댓값까지
    length = L[i + 1][0] - L[i][0]
    if height < L[i][1]:
        height = L[i][1]

    total_area += height * length

height = 0
for i in range(N - 1, L.index([pos_max, y_max]), -1):   # 오른쪽 끝에서 최댓값까지
    length = L[i][0] - L[i - 1][0]
    if height < L[i][1]:
        height = L[i][1]

    total_area += height * length

total_area += y_max

print(total_area)