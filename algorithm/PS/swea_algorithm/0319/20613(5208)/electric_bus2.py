def backtrack(pos, charged_cnt):     # pos : position, ev : left electricity
    global min_charge
    if pos >= M[0]:                 # if 종점
        min_charge = charged_cnt
        return

    charged_cnt += 1
    ev = M[pos]
    if charged_cnt >= min_charge:   # 최소 충전이 아닌 경우
        return

    for i in range(1, ev + 1):
        backtrack(pos + i, charged_cnt)


T = int(input())
for tc in range(1, T + 1):
    M = list(map(int, input().split()))     # M[1]: 1번 정류장 충전지
    min_charge = 100
    backtrack(1, -1)
    print(f'#{tc} {min_charge}')
