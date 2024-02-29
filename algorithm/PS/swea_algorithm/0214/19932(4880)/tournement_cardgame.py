def rsp(left, right):
    a = card[left]
    b = card[right]
    if a == 1 and b == 2:
        return right
    if a == 2 and b == 3:
        return right
    if a == 3 and b == 1:
        return right
    return left     # 비기거나 왼쪽이 이기면 왼쪽 리턴


def card_game_grouping(left, right):
    if left == right:          # 그루핑이 한명이 되었을 때
        return left
    elif left + 1 == right:    # 그루핑이 두 명이 되었을 때
        # 가위바위보 실행, 승자의 위치를 반환
        return rsp(left, right)
    else:
        left_group = card_game_grouping(left, (left + right) // 2)
        right_group = card_game_grouping((left + right) // 2 + 1, right)
        return rsp(left_group, right_group)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    card = list(map(int, input().split()))
    res = card_game_grouping(0, N - 1) + 1
    print(f'#{tc} {res}')
