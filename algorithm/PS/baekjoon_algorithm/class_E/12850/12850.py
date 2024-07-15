D = int(input())
# D 가 최대 10억이기에 단순 DP로 풀이하면 안될 것
# DP와 분할정복(제곱) 으로 풀이하면 될?듯
# 0: 정보과학, 1: 전산, 2: 미래, 3: 신양, 4: 진리,
# 5: 한경직기념, 6: 학생회, 7: 형남공학
graph = [
    [1, 2],         # 0
    [0, 2, 3],      # 1
    [0, 1, 3, 5],   # 2
    [1, 2, 4, 5],   # 3
    [3, 5, 6],      # 4
    [2, 3, 4, 7],   # 5
    [4, 7],         # 6
    [5, 6]          # 7
]

MOD = 1000000007

DP = [[0] * 2 for _ in range(8)]
DP[0][0] = 1
for i in range(D):
    # 매 횟수 다음 이동을 준비함
    for j in range(8):      # 이전 DP 값을 차원을 올려 저장하고 초기화
        DP[j][1] = DP[j][0]
        DP[j][0] = 0

    for j in range(8):
        for next_place in graph[j]:
            DP[next_place][0] = (DP[next_place][0] + DP[j][1]) % MOD

print(DP[0][0])
