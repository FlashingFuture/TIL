N = int(input())

max_5 = N // 5 + 1
max_3 = N // 3 + 1
res = - 1

for i in range(max_5):
    for j in range(max_3):
        if 5 * i + 3 * j == N:
            res = i + j

print(res)
