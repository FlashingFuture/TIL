N = int(input())
have = list(map(int, input().split()))
have.sort()
num_of_cards = {}
for h in have:
    if h not in num_of_cards:
        num_of_cards[h] = 1
    else:
        num_of_cards[h] += 1

M = int(input())
do_have = list(map(int, input().split()))
for n in do_have:
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if have[mid] == n:
            print(num_of_cards[n], end=' ')
            break

        elif have[mid] < n:
            start = mid + 1

        else:
            end = mid - 1

    if have[mid] != n:
        print(0, end=' ')
