from collections import deque


path = []
batting_orders = []


def ncr(n):
    if n == 9:
        batting_orders.append([path[x] for x in range(len(path))])
        return

    for i in range(9):
        if i in path: continue
        path.append(i)
        ncr(n + 1)
        path.pop()


ncr(0)

N = int(input())    # 이닝 수
innings = [deque(map(int, input().split()))]
base = deque([0, 0, 0])
point = 0
for players in innings:
    out_count = 0
    for hit in players:
        if hit == 1:
            base.append(1)
            point += base.popleft()
        elif hit == 2:
            base.append(1)
            base.append(0)
            point += base.popleft()
            point += base.popleft()
        elif hit == 3:
            base.append(1)
            base.append(0)
            base.append(0)
            point += base.popleft()
            point += base.popleft()
            point += base.popleft()
        elif hit == 4:
            base.append(1)
            base.append(0)
            base.append(0)
            base.append(0)
            point += base.popleft()
            point += base.popleft()
            point += base.popleft()
            point += base.popleft()
        else:
            out_count += 1

print(point)