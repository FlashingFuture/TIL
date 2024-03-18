import sys


N, M = map(int, input().split())
id_dict = {}
for i in range(N):
    site, my_id = sys.stdin.readline().split()
    id_dict[site] = my_id

for i in range(M):
    site = input()
    print(id_dict[site])