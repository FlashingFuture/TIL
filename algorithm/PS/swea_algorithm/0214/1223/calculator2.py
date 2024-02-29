ip = {'+': 1, '*': 2}


def transform_to_postfix(char):
    stack = []
    postfix = ''
    for item in char:
        if not stack and item in '+*':
            stack.append(item)

        elif item in '+*' and ip[item] > ip[stack[-1]]:     # input 우선순위가 높을때
            stack.append(item)

        elif item in '+*' and ip[item] <= ip[stack[-1]]:    # input 우선순위가 낮을때
            while stack and ip[item] <= ip[stack[-1]]:
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
        elif item == '*':
            temp = int(stack.pop())
            temp *= int(stack.pop())
            stack.append(temp)
        else:
            stack.append(item)

    return stack.pop()


for tc in range(1, 11):
    _ = int(input())    # 테스트 케이스의 길이
    arr = input()
    arr_postfix = transform_to_postfix(arr)
    res = postfix_calculation(arr_postfix)
    print(f'#{tc} {res}')
