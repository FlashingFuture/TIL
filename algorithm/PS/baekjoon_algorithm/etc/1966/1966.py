from collections import deque


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    importance = deque(list(map(int, input().split())))
    value = importance[M]
    importance[M] = -1
    cnt = 0
    while importance:
        temp = importance.popleft()
        if temp == -1:
            if importance and max(importance + deque([value])) > value:
                importance.append(temp)
            else:
                cnt += 1
                break
        else:
            if importance and max(importance + deque([value])) > temp:
                importance.append(temp)
            else:
                cnt += 1
    print(cnt)
