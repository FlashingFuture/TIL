T = int(input())
for tc in range(1, T + 1):
    n, hex_num = input().split()
    dec_num = int(hex_num, 16)
    reverse_str = ''
    for i in range(int(n) * 4):
        reverse_str += str(0b1 & dec_num)
        dec_num = dec_num >> 1

    res_str = reverse_str[::-1]
    print(f'#{tc} {res_str}')
