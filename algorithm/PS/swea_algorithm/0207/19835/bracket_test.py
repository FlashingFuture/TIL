T = int(input())
for tc in range(1, T + 1):
    code = input()
    stack = []
    result = 1
    for item in code:
        if item == '(':
            stack.append('(')

        elif item == '{':
            stack.append('{')

        elif item == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = 0
                break

        elif item == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                result = 0
                break

    if stack:
        result = 0

    print(f'#{tc} {result}')
