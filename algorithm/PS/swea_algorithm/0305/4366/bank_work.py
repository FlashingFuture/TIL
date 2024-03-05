def bi_trans(binary):
    decimal = 0
    for i in range(1, len(binary) + 1):
        decimal += int(binary[-i]) * (2 ** (i - 1))

    return decimal


def tri_trans(tri):
    decimal = 0
    for i in range(1, len(tri) + 1):
        decimal += int(tri[-i]) * (3 ** (i - 1))

    return decimal


def get_ans(bi, tr):
    for j in range(len(bi)):
        for k in range(len(tr)):
            if bi[j] == '1':
                bi[j] = '0'
            else:
                bi[j] = '1'

            temp1 = bi_trans(bi)

            if tr[k] == '0':
                tr[k] = '1'
                if temp1 == tri_trans(tr):
                    return temp1

                tr[k] = '2'
                if temp1 == tri_trans(tr):
                    return temp1

                tr[k] = '0'

            if tr[k] == '1':
                tr[k] = '0'
                if temp1 == tri_trans(tr):
                    return temp1

                tr[k] = '2'
                if temp1 == tri_trans(tr):
                    return temp1

                tr[k] = '1'

            if tr[k] == '2':
                tr[k] = '0'
                if temp1 == tri_trans(tr):
                    return temp1

                tr[k] = '1'
                if temp1 == tri_trans(tr):
                    return temp1

                tr[k] = '2'

            if bi[j] == '1':
                bi[j] = '0'
            else:
                bi[j] = '1'

    return 0


T = int(input())
for tc in range(1, T + 1):
    bi_num = input()
    tri_num = input()
    binary_list = [bi_num[x] for x in range(len(bi_num))]
    tri_list = [tri_num[x] for x in range(len(tri_num))]
    res = get_ans(binary_list, tri_list)
    print(f'#{tc} {res}')
