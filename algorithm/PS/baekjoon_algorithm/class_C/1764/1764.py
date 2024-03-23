import sys


N, M = map(int, sys.stdin.readline().split())
not_listened = {}
for i in range(N):
    name = sys.stdin.readline().strip()
    not_listened[name] = 1

for i in range(M):
    name = sys.stdin.readline().strip()
    if name in not_listened:
        not_listened[name] += 1

not_listened_seen = []
for k, v in not_listened.items():
    if v == 2:
        not_listened_seen.append(k)

not_listened_seen.sort()
print(len(not_listened_seen))
for i in range(len(not_listened_seen)):
    print(not_listened_seen[i])
