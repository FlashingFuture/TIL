import sys


N = int(sys.stdin.readline())
R, G, B = [0] * N, [0] * N, [0] * N
for i in range(N):
    R[i], G[i], B[i] = map(int, sys.stdin.readline().split())
# 각 집마다
# 해당 색깔일 때 최솟값으로 도달하는 값을
# dp를 통해 구하면 될듯
r_min = R[0]
g_min = G[0]
b_min = B[0]
for i in range(1, N):
    next_r_min = min(g_min, b_min)
    next_g_min = min(r_min, b_min)
    next_b_min = min(r_min, g_min)
    r_min = next_r_min + R[i]
    g_min = next_g_min + G[i]
    b_min = next_b_min + B[i]

res = min(r_min, g_min, b_min)
print(res)
