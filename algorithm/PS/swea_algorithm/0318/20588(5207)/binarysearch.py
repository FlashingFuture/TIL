def find_turned_index(s, e, last):  # last==0:지난번에 왼쪽, 1:지난번에 오른쪽
    if s <= e:
        mid = (s + e) // 2
        ans_list.append(A[mid])
        if last == 0:
            find_turned_index(mid+1, e, 1)
        else:
            find_turned_index(s, mid-1, 0)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    ans_list = []
    find_turned_index(0, N - 1, 0)
    find_turned_index(0, (N - 1) // 2 - 1, 0)
    res = 0
    for item in B:
        if item in ans_list:
            res += 1

    print(f'#{tc} {res}')
