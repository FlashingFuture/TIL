N, M, K = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
min_sum = 99999999
print()
for _ in range(K):
    r, c, s = map(int, input().split())
    temp_array = [[array[y][x] for x in range(M)] for y in range(N)]
    # 시계 방향 90도 회전
    # 중심으로 잡을 회전하는 사각형의 왼쪽 위 꼭짓점
    y, x = r - s - 1, c - s - 1
    for i in range(2*s + 1):
        for j in range(2*s + 1):
            temp_array[j + y][2*s - i + x] = array[i + y][j + x]

    for i in range(N):
        min_sum = min(min_sum, sum(temp_array[i]))

print(min_sum)