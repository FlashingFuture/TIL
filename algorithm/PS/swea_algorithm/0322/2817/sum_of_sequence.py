# 1. 완전탐색
# N개 중에서 조합하여 합을 구하는 경우의 수를 다 더하면
# nC0 + nC1 + ... + ncn = 2^n
# 2^20 = 1,024*1,024 < 2,000,000
# 따라서 20개 테스트케이스를 합쳐도 40,000,000이 안됨. 충분
# 하지만 백트래킹을 해서 가지치기를 해주면 더 좋다
def backtrack(lev, sum_num):
    if sum_num == K:
        global res_cnt
        res_cnt += 1
        return

    if sum_num > K or lev >= N:
        return
    # 다음 숫자를 더하거나 안 더하거나
    backtrack(lev + 1, sum_num)
    backtrack(lev + 1, sum_num + A[lev])


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    res_cnt = 0
    backtrack(0, 0)
    print(f'#{tc} {res_cnt}')
