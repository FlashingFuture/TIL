def transform_to_postfix(char):
    stack = []
    postfix = ''
    for item in char:
        if item == '+':
            if stack and stack[-1] == item:
                postfix += stack.pop()
            stack.append(item)

        else:
            postfix += item

    while stack:
        postfix += stack.pop()
    return postfix


def postfix_calculation(char):
    stack = []
    result = 0
    for item in char:
        if item == '+':
            temp = int(stack.pop())
            temp += int(stack.pop())
            stack.append(temp)
        else:
            stack.append(item)

    return stack.pop()


for tc in range(1, 11):
    _ = int(input())
    arr = input()   # 계산할 문자열
    pos = transform_to_postfix(arr)
    res = postfix_calculation(pos)
    print(f'#{tc} {res}')
