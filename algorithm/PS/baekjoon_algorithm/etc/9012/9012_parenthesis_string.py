def is_vps(arr):
    stack = []
    for item in arr:
        if item == '(':
            stack.append(item)
        elif item == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print('NO')
                return

    if stack:
        print('NO')
        return

    print('YES')
    return


T = int(input())
for _ in range(T):
    char = input()
    is_vps(char)
