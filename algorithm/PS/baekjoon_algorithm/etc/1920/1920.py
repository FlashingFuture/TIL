N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()
for item in B:
    L = 0  # left
    R = len(A) - 1      # right
    res = 0
    while L <= R:
        mid = (L + R) // 2
        if A[mid] == item:
            res = 1
            break

        elif A[mid] < item:
            L = mid + 1

        else:
            R = mid - 1

    print(res)
    