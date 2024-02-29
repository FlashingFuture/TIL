N, K = map(int, input().split())        # N : 총 학생 수, K : 한 방의 수용인원
count = [[0] * 2 for _ in range(6)]     # 성별 / 학년으로 나눠줄 2x6 카운트 배열
for i in range(N):
    S, Y = map(int, input().split())        # S : 성별, Y = year(학년)
    count[Y - 1][S] += 1

res = 0
for i in range(2):
    for j in range(6):
        res += count[j][i] // K
        if count != 0 and count[j][i] % K != 0:
            res += 1

print(res)

