from collections import deque


def toggle(n):
    if n == 1:
        return 0
    else:
        return 1


T = int(input())
for tc in range(1, T + 1):
    p = input()
    n = int(input())
    char_x = input()
    x = deque([])
    try:
        if n == 0:
            if 'D' not in p:
                print('[]')
            else:
                print('error')
            continue

        else:
            temp = char_x[1:-1]
            temp_queue = list(temp.split(','))
            for item in temp_queue:
                x.append(item)

        t_cnt = 0       # 토글 카운터
        pop_cnt = [0] * 2
        for item in p:
            if item == 'R':
                t_cnt = toggle(t_cnt)

            elif item == 'D':
                pop_cnt[t_cnt] += 1

        for i in range(pop_cnt[0]):
            x.popleft()

        for i in range(pop_cnt[1]):
            x.pop()

        res = deque([])
        if t_cnt == 1:
            while x:
                res.appendleft(x.popleft())
                res.appendleft(',')
            if res:
                res.popleft()
        else:
            while x:
                res.appendleft(x.pop())
                res.appendleft(',')
            if res:
                res.popleft()

        print('[', end='')
        if res:
            print(''.join(res), end='')
        print(']')

    except:
        print('error')
