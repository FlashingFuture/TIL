N = int(input())

arr = [['*'] * (4*N - 3) for _ in range(4*N - 1)]

pos = [1, 4*N - 4]
k = 0               # 뱀처럼 돌기 위해 카운트를 세줄 변수
while True:
    while pos[1] > 1 + k:       # <-
        arr[pos[0]][pos[1]] = ' '
        pos[1] -= 1

    while pos[0] < 4*N - 3 - k:     # down
        arr[pos[0]][pos[1]] = ' '
        pos[0] += 1

    while pos[1] < 4*N - 5 - k:     # ->
        arr[pos[0]][pos[1]] = ' '
        pos[1] += 1

    k += 2
    while pos[0] > 1 + k:           # up
        arr[pos[0]][pos[1]] = ' '
        pos[0] -= 1

    if k // 2 >= N - 1:
        arr[pos[0]][pos[1]] = ' '
        break

if N == 1:
    print('*')
else:
    for _ in range(1, 4*N - 3):
        arr[1].pop()
    for i in range(4*N - 1):
        print(''.join(arr[i]))
