import sys


N = int(sys.stdin.readline())
my_list = [[0, 0] for _ in range(N)]
for i in range(N):
    my_list[i][0], my_list[i][1] = map(int, sys.stdin.readline().split())

my_list.sort(key=lambda x: (x[0], x[1]))
for i in range(N):
    print(my_list[i][0], my_list[i][1])
