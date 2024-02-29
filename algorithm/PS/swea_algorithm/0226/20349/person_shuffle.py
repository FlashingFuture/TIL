from collections import deque


def overhand(cards):
    for _ in range(len(cards) * 37 // 100):
        cards.appendleft(cards.pop())

    return cards


def perfect(cards):
    temp = deque()
    for _ in range(len(cards) // 2):
        temp.appendleft(cards.pop())

    shuffled = deque()
    for _ in range(len(temp)):
        shuffled.append(cards.popleft())
        shuffled.append(temp.popleft())

    if cards:
        shuffled.append(cards.pop())

    return shuffled


TC = int(input())
for tc in range(1, TC + 1):
    N, T = map(int, input().split())
    card = deque(list(k for k in range(1, N + 1)))
    for i in range(T):
        card = overhand(card)
        card = perfect(card)

    print(f'#{tc}', end=' ')
    print(*card)
