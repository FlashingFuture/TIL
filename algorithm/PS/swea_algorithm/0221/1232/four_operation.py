def postorder(t):
    global word
    if c[t]:
        postorder(int(c[t][0]))
        if len(c[t]) >= 2:
            postorder(int(c[t][1]))
    word.append(t_val[t])


def postfix_calc(postfix):
    stack = []
    for item in postfix:
        if item.isnumeric():
            stack.append(int(item))
        else:
            if item == '+':
                temp = stack.pop() + stack.pop()
                stack.append(temp)
            elif item == '-':
                temp = stack.pop() - stack.pop()
                stack.append(-temp)
            elif item == '*':
                temp = stack.pop() * stack.pop()
                stack.append(temp)
            elif item == '/':
                temp = stack.pop()
                temp = stack.pop() // temp
                stack.append(temp)

    return stack[0]


for tc in range(1, 11):
    N = int(input())
    t_val = [None] * (N + 1)
    c = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        arr = input().split()
        t_val[i] = arr[1]
        if len(arr) >= 3:
            c[i].append(arr[2])
            if len(arr) >= 4:
                c[i].append(arr[3])

    word = []
    postorder(1)
    res = postfix_calc(word)
    print(f'#{tc} {res}')