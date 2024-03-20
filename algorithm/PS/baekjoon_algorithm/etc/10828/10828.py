import sys


N = int(sys.stdin.readline())
order = [sys.stdin.readline().split() for _ in range(N)]
stack = []
for item in order:
    if item[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif item[0] == 'push':
        stack.append(item[1])

    elif item[0] == 'size':
        print(len(stack))

    elif item[0] == 'top':
        if stack:
            if len(stack) > 1:
                print(stack[-1])
            else:
                print(stack[0])
        else:
            print(-1)

    elif item[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)