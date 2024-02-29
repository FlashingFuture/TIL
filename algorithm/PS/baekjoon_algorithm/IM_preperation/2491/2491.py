from collections import deque

N = int(input())
arr = list(map(int, input().split()))

up_que = deque([arr[0]])
up_cnt = 0
down_que = deque([arr[0]])
down_cnt = 0
max_counts = [1]
for item in arr:
    up_que.append(item)
    if item >= up_que.popleft():
        up_cnt += 1
    else:
        max_counts.append(up_cnt)
        up_cnt = 1

    down_que.append(item)
    if item <= down_que.popleft():
        down_cnt += 1
    else:
        max_counts.append(down_cnt)
        down_cnt = 1

max_counts.append(up_cnt)
max_counts.append(down_cnt)
print(max(max_counts))