def selection_sort(arr):
    for i in range(0, len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))
    sorted_a = selection_sort(a)
    print(f'#{tc}', end=' ')
    for i in range(5):
        print(sorted_a[N - i - 1], end=' ')
        print(sorted_a[i], end=' ')

    print()
