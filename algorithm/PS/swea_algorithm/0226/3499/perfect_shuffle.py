T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    card = input().split()
    odd_pointer = 0
    even_pointer = (N + 1) // 2
    shuffled_card = []
    for _ in range(N // 2):
        shuffled_card.append(card[odd_pointer])
        shuffled_card.append(card[even_pointer])
        odd_pointer += 1
        even_pointer += 1

    if N % 2 == 1:
        shuffled_card.append(card[odd_pointer])

    print(f'#{tc}', end=' ')
    print(*shuffled_card)