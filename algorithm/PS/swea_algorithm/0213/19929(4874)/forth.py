def forth_calculation(arr):
    stack = []
    for item in arr:
        try:
            if item == '+':
                temp = stack.pop()
                temp += stack.pop()
                stack.append(temp)

            elif item == '-':
                temp = stack.pop()
                temp2 = stack.pop()
                temp2 -= temp
                stack.append(temp2)

            elif item == '*':
                temp = stack.pop()
                temp *= stack.pop()
                stack.append(temp)

            elif item == '/':
                temp = stack.pop()
                temp2 = stack.pop()
                temp2 //= temp
                stack.append(temp2)

            elif item == '.':
                return stack.pop()

            else:
                stack.append(int(item))

        except IndexError:
            return 'error'

    return 'error'


T = int(input())
for tc in range(1, T + 1):
    char_list = input().split()
    res = forth_calculation(char_list)
    print(f'#{tc} {res}')
