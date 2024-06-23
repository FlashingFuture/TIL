import sys


M = int(input())
my_set = set()
for i in range(M):
    order = list(sys.stdin.readline().split())
    if order[0] == 'add':
        my_set.add(int(order[1]))
    elif order[0] == 'remove':
        my_set.discard(int(order[1]))
    elif order[0] == 'check':
        print(1) if int(order[1]) in my_set else print(0)
    elif order[0] == 'toggle':
        if int(order[1]) in my_set:
            my_set.remove(int(order[1]))
        else:
            my_set.add(int(order[1]))
    elif order[0] == 'all':
        my_set = set(range(1, 21))
    elif order[0] == 'empty':
        my_set.clear()
