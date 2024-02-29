from collections import deque

N = int(input())

for i in range(N):
    arr = deque(['* ' * N])
    if i % 2 == 1:  # 짝수 번째 열이라면
        arr.appendleft(' ')

    print(''.join(arr))
