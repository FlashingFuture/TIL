T = int(input())
for tc in range(T):     # T만큼 테스트 케이스 반복
    s = input()

    stack = [s[0]]
    for i in range(1, len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])

    print(f'#{tc + 1} {len(stack)}')
