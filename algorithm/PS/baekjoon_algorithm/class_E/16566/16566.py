import sys


N, M, K = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
opponent_cards = list(map(int, sys.stdin.readline().split()))

# cards 를 정렬하고, 철수의 입력에 대해 그보다 큰 값을 찾는다
# 이분 탐색으로 이동하되, 같거나 때까지 이동하다 같아지면 break
# 그 후 카드에서 사용 카드를 빼야 하는데 진짜로 빼버리면 시간복잡도 4000000므로
# disabled 배열을 따로 만들어 거기서 빠진 카드인지 확인할 수 있도록 함
# 이진탐색 자체는 한 회당 log(4000000) = 22 정도로 걸릴 것
cards.sort()                    # 시간복잡도 : 4000000 * 22
disabled = [0] * (M + 1)        # 이진탐색으로 정답을 찾았을 때 빠진 카드를 계산해 정답을 도출
cards.append(sys.maxsize)       # 로직을 위해 cards 끝에 maxsize append
cards.insert(0, -sys.maxsize)   # 로직을 위해 cards 시작에 -maxsize append
# cards 는 [-maxsize, ... , maxsize]의 형태가 되어
# 이진탐색 시 결국 idx 1 ~ M 사이에서 모든 값을 찾게 됨(문제 조건에 따름)
for op_card in opponent_cards:   # 철수가 내는 모든 카드에 대해
    # 이진탐색 진행
    start = 0
    end = M
    while start <= end:
        mid = (start + end) // 2
        my_card = cards[mid]
        my_card_next = cards[mid + 1]
        if my_card <= op_card <= my_card_next:  # 낼 수 있는 최저의 카드를 찾은 경우
            while my_card < sys.maxsize:
                if my_card > op_card:       # mid 를 1씩 늘려가며 낼 수있는 카드를 찾음
                    if not disabled[mid]:
                        print(my_card)
                        disabled[mid] = 1
                        break
                mid += 1
                my_card = cards[mid]
            break

        elif my_card > op_card:
            end = mid - 1
        elif my_card < op_card:
            start = mid + 1
