N, M = map(int, input().split())
card = list(map(int, input().split()))
# N개 중 3개를 골라 합을 구해 저장한다
path = []
sum_list = []


def comb(lev, start):
    if lev == 3:
        temp = sum(card[x] for x in path)
        if temp <= M:
            sum_list.append(temp)
        return

    for i in range(start, N):
        path.append(i)
        comb(lev + 1, i + 1)
        path.pop()


comb(0, 0)
print(max(sum_list))
