N = int(input())
member = []
for _ in range(N):
    a, n = input().split()
    member.append((int(a), n))

member.sort(key=lambda x: x[0])
for i in range(N):
    print(*member[i])