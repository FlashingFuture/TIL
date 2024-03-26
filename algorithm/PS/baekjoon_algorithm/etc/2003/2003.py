import sys


N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))


def two_pointer():
    start, end = 0, 0
    temp = 0
    global cnt
    while start < N:
        while temp < M and end < N:
            temp += A[end]
            end += 1

        if temp == M:
            cnt += 1

        temp -= A[start]
        start += 1


cnt = 0
two_pointer()
print(cnt)
