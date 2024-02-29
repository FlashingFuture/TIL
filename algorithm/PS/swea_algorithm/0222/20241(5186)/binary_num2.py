T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    div_num = 1 / 2
    res = ''
    overflow = True
    for i in range(12):
        if N > div_num:
            N -= div_num
            res += '1'
            div_num /= 2
        elif N == div_num:
            res += '1'
            overflow = False
            break
        else:
            res += '0'
            div_num /= 2

    if overflow:
        res = 'overflow'

    print(f'#{tc} {res}')
