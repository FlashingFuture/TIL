import sys


N, M, K = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
opponent_cards = list(map(int, sys.stdin.readline().split()))

# cards를 정렬하고, 철수의 입력에 대해 그보다 큰 값을 찾는다
# 이분 탐색으로 이동하되, 같거나 때까지 이동하다 같아지면 break
# 그 후 카드에서 사용 카드를 빼야 하는데 진짜로 빼버리면 시간복잡도 4000000
cards.sort()                    # 시간복잡도 : 4000000 * 22
disabled = [0] * (M + 2)        # 이분탐색으로 정답을 찾았을 때 빠진 카드를 계산해 정답을 도출
cards.append(sys.maxsize)       # 로직을 위해 cards 끝에 maxsize append
cards.insert(0, -sys.maxsize)   # 로직을 위해 cards 시작에 -maxsize append
debug_list = []
for op_card in opponent_cards:   # 철수가 내는 모든 카드에 대해
    start = 0
    end = N
    while start <= end:
        mid = (start + end + 1) // 2
        my_card = cards[mid]
        my_card_next = cards[mid + 1]
        if my_card <= op_card <= my_card_next:
            while my_card < sys.maxsize:
                if my_card > op_card:
                    if not disabled[mid]:
                        print(my_card)
                        debug_list.append(my_card)
                        disabled[mid] = 1
                        break
                mid += 1
                my_card = cards[mid]
            break

        elif my_card > op_card:
            end = mid - 1
        elif my_card < op_card:
            start = mid + 1
