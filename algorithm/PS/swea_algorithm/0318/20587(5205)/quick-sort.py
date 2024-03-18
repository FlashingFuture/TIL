def quicksort(s, e):
    if s < e:
        p = swap(s, e)
        quicksort(s, p - 1)
        quicksort(p + 1, e)


def swap(start, end):
    pivot = arr[start]
    i = start
    j = end
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1

        while i <= j and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[start], arr[j] = arr[j], arr[start]

    return j


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quicksort(0, N - 1)
    print(f'#{tc} {arr[N // 2]}')