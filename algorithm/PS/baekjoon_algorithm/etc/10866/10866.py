from collections import deque
import sys


N = int(sys.stdin.readline())
my_deque = deque([])
for _ in range(N):
    o = sys.stdin.readline().split()
    if o[0] == 'push_back':
        my_deque.append(o[1])

    elif o[0] == 'push_front':
        my_deque.appendleft(o[1])

    elif o[0] == 'pop_front':
        if my_deque:
            print(my_deque.popleft())
        else:
            print(-1)

    elif o[0] == 'pop_back':
        if my_deque:
            print(my_deque.pop())
        else:
            print(-1)

    elif o[0] == 'size':
        print(len(my_deque))

    elif o[0] == 'empty':
        if my_deque:
            print(0)
        else:
            print(1)

    elif o[0] == 'front':
        if my_deque:
            temp = my_deque.popleft()
            print(temp)
            my_deque.appendleft(temp)
        else:
            print(-1)

    elif o[0] == 'back':
        if my_deque:
            temp = my_deque.pop()
            print(temp)
            my_deque.append(temp)
        else:
            print(-1)
