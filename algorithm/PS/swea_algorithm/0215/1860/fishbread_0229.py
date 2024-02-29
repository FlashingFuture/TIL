T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    P = list(map(int, input().split()))

    P.sort()    # 내림차순 정렬을 이용해 시간 순서대로 문제풀이
    sold_bread = 0
    can_sell = True
    for p in P:
        made_bread = (p // M) * K
        sold_bread += 1
        remain = made_bread - sold_bread
        if remain < 0:
            can_sell = False
            break

    if can_sell:
        res = 'Possible'
    else:
        res = 'Impossible'

    print(f'#{tc} {res}')