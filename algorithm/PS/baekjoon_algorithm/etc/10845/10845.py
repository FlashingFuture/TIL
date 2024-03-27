from collections import deque
import sys


N = int(sys.stdin.readline())
queue = deque([])
order = []
for i in range(N):
    order.append(sys.stdin.readline().split())

for item in order:
    if item[0] == 'push':
        queue.append(item[1])

    elif item[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif item[0] == 'size':
        print(len(queue))

    elif item[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)

    elif item[0] == 'front':
        if queue:
            temp = queue.popleft()
            print(temp)
            queue.appendleft(temp)
        else:
            print(-1)

    elif item[0] == 'back':
        if queue:
            temp = queue.pop()
            print(temp)
            queue.append(temp)
        else:
            print(-1)
