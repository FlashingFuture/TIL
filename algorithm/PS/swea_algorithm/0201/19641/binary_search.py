def binary_search(volume, target_page):
    first = 1
    last = volume
    cnt = 0
    while last >= first:
        cnt += 1
        middle = (first + last) // 2
        if middle < target_page:
            first = middle
        elif middle == target_page:
            return cnt
        else:
            last = middle

    return False


T = int(input())
for tc in range(1, T + 1):  # t만큼 테스트 반복
    P, Pa, Pb = map(int, input().split())
    timeA = binary_search(P, Pa)
    timeB = binary_search(P, Pb)

    if timeA < timeB:
        print(f'#{tc} A')
    elif timeA == timeB:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} B')
