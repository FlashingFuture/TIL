import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())
chart = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
friends = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
chart_copied = [[chart[i][j] for j in range(n)] for i in range(n)]

queue = deque([])

