# DP
# 1. 작은 문제로 분할
# - 전체의 합 : 각 달까지의 최소값들이 쌓이면서 완성됨
# 2. 뒤의 결과를 구할 때, 앞에서 구한 결과가 바뀌지 않음


T = int(input())
for tc in range(1, T + 1):
    D, M, Q, Y = map(int, input().split())      # daily, monthly, quarterly, yearly
    days = [0] + list(map(int, input().split()))
    plans = [0] * 13
    
    for i in range(1, 13):
        # 현재 달의 최소 비용 계산
        # 이전 달 + (1일 or 1달) / 3달 전 + 3달권 중 최소
        case1 = plans[i - 1] + days[i] * D
        case2 = plans[i - 1] + M
        case3 = Y
        if i >= 3:
            case3 = plans[i - 3] + Q

        plans[i] = min(case1, case2, case3)

    min_cost = min(plans[12], Y)
    print(f'#{tc} {min_cost}')
