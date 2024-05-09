import sys
path = []
ans_list = []


def backtrack(lev, start):
    if lev == M:
        if path not in ans_list:
            ans_list.append([path[x] for x in range(M)])

    for i in range(start, N):
        path.append(arr[i])
        backtrack(lev + 1, i + 1)
        path.pop()


N, M = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

backtrack(0, 0)

for ans_path in ans_list:
    print(*ans_path)