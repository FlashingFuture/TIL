path = []


def backtrack(total, s):
    if total >= B:
        global res
        res = min(total - B, res)
        return

    for i in range(s, N):
        path.append(i)
        backtrack(total + H[i], i + 1)
        path.pop()


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    res = 9999
    backtrack(0, 0)
    print(f'#{tc} {res}')