def en_heap(n):     # 최소힙
    global last  # 마지막 노드 추가(완전이진트리 유지)
    last += 1
    heap[last] = n  # 마지막 노드에 데이터 삽입
    child = last
    parent = child // 2
    while parent and heap[parent] > heap[child]:  # 부모가 있고, 부모값이 더 크다면
        heap[parent], heap[child] = heap[child], heap[parent]  # 교환
        child = parent
        parent = child // 2


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    heap = [0] * (N + 1)
    last = 0
    for item in arr:
        en_heap(item)

    # 조상 다 더하기
    sum_of_anc = 0
    while N >= 1:
        N //= 2
        sum_of_anc += heap[N]

    print(f'#{tc} {sum_of_anc}')
