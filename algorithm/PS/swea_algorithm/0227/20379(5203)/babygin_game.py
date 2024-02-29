from collections import deque


path = []
visited = [0] * 10


def bg_recur(n, player, k):        # n : 재귀를 돌 숫자, k : 입력받은 카드의 개수
    global win
    if n == 3:
        if player[path[0]] == player[path[1]] == player[path[2]]:
            win = 1
        elif player[path[0]] == player[path[1]] - 1 == player[path[2]] - 2:
            win = 1
        return

    for i in range(k):
        if visited[i]: continue
        visited[i] = 1
        path.append(i)
        bg_recur(n + 1, player, k)
        path.pop()
        visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    card = deque(map(int, input().split()))
    p1, p2 = [], []
    win = 0
    res = 0
    while card and not win:
        p1.append(card.popleft())
        p2.append(card.popleft())
        if len(p1) >= 3:
            bg_recur(0, p1, len(p1))
            if win == 1:
                res = 1
                break

            bg_recur(0, p2, len(p2))
            if win == 1:
                res = 2
                break

    print(f'#{tc} {res}')