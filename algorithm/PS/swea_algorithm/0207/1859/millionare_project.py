T = int(input())
for tc in range(1, T + 1):  # 테스트케이스 T번 반복
    N = int(input())
    prices = list(map(int, input().split()))    # 모든 날의 값 리스트
    margin = 0                          # 마진의 합
    max_num = 0                         # 오른쪽부터 최댓값을 셀 변수
    for i in range(N - 1, -1, -1):
        if max_num < prices[i]:
            max_num = prices[i]         # 최댓값을 max_num에 할당

        margin += max_num - prices[i]   # 마진에 더해줌

    print(f'#{tc} {margin}')