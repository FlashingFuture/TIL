from collections import deque


dz = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dx = [0, 0, 0, 0, 1, -1]


M, N, H = map(int, input().split())
T = [[list(map(int, input().split())) for _ in range(N)] for __ in range(H)]


def bfs(z, y, x):
    queue = deque([])
