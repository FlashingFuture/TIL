path = []
combs = []


def comb(lev, start):
    if lev == (N // 2):
        combs.append([path[x] for x in range(N//2)])

    for i in range(start, N):
        path.append(i)
        comb(lev + 1, i + 1)
        path.pop()


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
# 팀 생성은 N개 중 N // 2 개를 고르는 조합의 경우가 전부
res = 99999
comb(0, 0)
for j in range(len(combs) // 2):
    team1 = combs[j]
    team2 = [x for x in range(N) if x not in team1]
    total1 = 0
    for k in range(len(team1)):
        for L in range(len(team1)):
            if k == L:
                continue
            total1 += S[team1[k]][team1[L]]

    total2 = 0
    for k in range(len(team2)):
        for L in range(len(team2)):
            if k == L:
                continue
            total2 += S[team2[k]][team2[L]]

    temp = abs(total1 - total2)
    if temp < res:
        res = temp

print(res)
