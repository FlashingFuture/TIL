import sys


N, K = map(int, sys.stdin.readline().split())
A = [int(sys.stdin.readline()) for _ in range(N)]
# 필요 동전 개수의 최솟값을 구하기 위해
# bfs로 탐색하면서 해당 값에 도달하기
# 1억이니까 완전탐색 시 이론적으로 시간초과가 남
# 차라리 백트래킹?
# 운이 없으면 시간초과 아닌가?
# 동전은 모두 그보다 작은 동전의 배수이기에
# 큰놈부터 고르면 그냥 해결되는 문제였다
A.sort(reverse=True)    # 큰 수부터 빼주기 위해 내림차순으로 정렬
cnt = 0
for coin in A:
    while coin <= K:
        K -= coin
        cnt += 1

print(cnt)
