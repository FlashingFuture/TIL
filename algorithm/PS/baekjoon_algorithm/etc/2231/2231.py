N = int(input())
res = 0
for i in range(N, (N // 2) - 1, -1):
    temp = i
    total = i
    while temp:
        total += temp % 10
        temp //= 10

    if total == N:
        res = i

print(res)