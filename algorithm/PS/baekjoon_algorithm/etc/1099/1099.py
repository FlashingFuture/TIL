from collections import deque


char = input()
N = int(input())
words = [input() for _ in range(N)]
res = 0
for word in words:
    for alphabet in word:
        if alphabet not in char:
            res = -1
            break

    if len(word) > len(char):
        res = -1
        break

    if res == -1:
        break

    cost = 0
    for i in range(len(word)):
        if char[i] != word[i]:
            cost += 1

    min_cost = cost
    for k in range(1, len(char) - len(word)):
        cost = 0
        for i in range(len(word)):
            if char[k + i] != word[i]:
                cost += 1

        if min_cost > cost:
            min_cost = cost

    res += min_cost

print(res)