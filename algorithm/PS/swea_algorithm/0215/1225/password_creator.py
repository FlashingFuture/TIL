from collections import deque

while True:
    try:
        tc = int(input())
    except EOFError:
        break

    arr = list(map(int, input().split()))
    pw_list = deque(arr)
    breaker = 0         # for문 내부에서 0을 감지하면 while문을 break하기 위한 변수
    while True:
        for i in range(1, 6):
            temp = pw_list.popleft() - i

            pw_list.append(temp)
            if temp <= 0:
                pw_list[7] = 0
                breaker = 1
                break

        if breaker == 1:
            break

    print(f'#{tc}', end=' ')
    for item in pw_list:
        print(item, end=' ')

    print()