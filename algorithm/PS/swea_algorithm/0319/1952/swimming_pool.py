def backtrack(lev, cost):
    global min_cost
    if cost >= min_cost:
        return

    if lev >= 12:
        min_cost = cost
        return

    # 다음 달 한달만 결제 : 1일 이용권, 1달 이용권은 양립할 수 없음!
    if plan[lev] * D < M:
        backtrack(lev + 1, cost + plan[lev] * D)
    else:
        backtrack(lev + 1, cost + M)

    # 세 달 결제
    backtrack(lev + 3, cost + Q)


T = int(input())
for tc in range(1, T + 1):
    D, M, Q, Y = map(int, input().split())  # day, month, quarter, year 이용권 가격
    plan = list(map(int, input().split()))
    min_cost = Y        # default min cost : year 이용권
    backtrack(0, 0)
    print(f'#{tc} {min_cost}')
