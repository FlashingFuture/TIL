import sys


if __name__ == '__main__':
    N, S = map(int, input().split())
    arr = list(map(int, sys.stdin.readline().split()))
    start, end = 0, 0
    temp_sum = 0
    min_length = sys.maxsize
    while end < N:
        if temp_sum < S:
            temp_sum += arr[end]
            end += 1
        else:
            min_length = min(min_length, end - start)
            temp_sum -= arr[start]
            start += 1

    while start < N and temp_sum >= S:
        min_length = min(min_length, end - start)
        temp_sum -= arr[start]
        start += 1

    if min_length == sys.maxsize:
        min_length = 0

    print(min_length)


# 풀이
# 가장 짧은 부분합의 길이를 찾아야 하므로 투 포인터로 찾으면서
# 최소 길이도 기록하면서 움직이면 될 것
