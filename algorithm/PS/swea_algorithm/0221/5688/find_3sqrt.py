def find_3sqrt(n):
    start = 1
    end = int(n**(1 / 3)) + 1
    while start <= end:
        mid = (start + end) // 2
        if mid**3 == n:
            return mid
        elif mid**3 < n:
            start = mid + 1
        else:
            end = mid - 1

    return -1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    res = find_3sqrt(N)

    print(f'#{tc} {res}')