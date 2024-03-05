N, M = map(int, input().split())
island = [list(map(int, input().split())) for _ in range(7)]
# 가능한 모든 다리를 만든 뒤에 그 중 가장 최소인 경우를 백트래킹으로 탐색
