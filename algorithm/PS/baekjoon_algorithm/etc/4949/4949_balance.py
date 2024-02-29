while True:
    try:
        C = input()
    except EOFError:
        break

    if C == '.':
        break

    stack = []
    balance = 'yes'
    for c in C:
        if c in '([':
            stack.append(c)

        elif c == ')':
            if stack:
                if stack.pop() != '(':
                    balance = 'no'
                    break
            else:
                balance = 'no'
                break

        elif c == ']':
            if stack:
                if stack.pop() != '[':
                    balance = 'no'
                    break
            else:
                balance = 'no'
                break

    if stack:
        balance = 'no'
    print(balance)
