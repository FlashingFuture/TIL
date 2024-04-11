path = []


N, M = map(int, input().split())
A = list(map(int, input().split()))
a_count = {}
for num in A:
    if num in a_count:
        a_count[num] += 1
    else:
        a_count[num] = 1

A = list(set(A))
A.sort()


def backtrack():
    if len(path) == M:
        print(*path)
        return

    for a in A:
        if path.count(a) < a_count[a]:
            path.append(a)
            backtrack()
            path.pop()


backtrack()