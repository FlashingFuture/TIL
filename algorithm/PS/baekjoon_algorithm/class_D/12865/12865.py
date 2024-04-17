N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
# item[i][0]: 무게, item[i][1]: 가치
# 각 무게에 대한 최댓값 배열을 만들어 DP로 풀이
# 100001 x 100 = 10000100으로 0.1초 정도가 소모될 것으로 예상
items.sort(key=lambda x: x[1] / x[0])    # 무게 대비 가치 순으로 정렬
DP = [0] * (K + 1)
LAST_DP = [0] * (K + 1)
for item in items:
    for i in range(K + 1):
        if i == 0 or LAST_DP[i] > 0:     # 0이나 이미 값이 들어온 지점에 대해
            if i + item[0] <= K and LAST_DP[i + item[0]] < LAST_DP[i] + item[1]:    # 무게를 초과하지 않고 최대값이 갱신될 때
                DP[i + item[0]] = LAST_DP[i] + item[1]

    for i in range(K + 1):
        LAST_DP[i] = DP[i]

print(max(DP))
