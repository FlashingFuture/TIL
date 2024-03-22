import sys


N = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(N)]
num.sort()
for i in range(N):
    print(num[i])