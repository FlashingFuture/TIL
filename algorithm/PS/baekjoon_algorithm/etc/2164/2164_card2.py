from collections import deque


N = int(input())
cards = deque([x for x in range(1, N + 1)])
for i in range(N - 1):
    cards.popleft()
    cards.append(cards.popleft())

print(*cards)
