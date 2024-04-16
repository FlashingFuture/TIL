# 방법 1
# 0.1초 : 최대 천만 번 연산?

char1 = input()
char2 = input()
N = len(char1)
M = len(char2)
res = 0
for i in range(N):
    for j in range(M):
        if char1[i] == char2[j]:
            count = 1
            y, x = i + 1, j + 1
            while y < N and x < M:
                if char1[y] == char2[x]:
                    print(char1[y], char2[x], count)
                    count += 1
                    y += 1
                    x += 1
                else:
                    x += 1
            res = max(res, count)

print(res)