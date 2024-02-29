def hex_to_bin(hex_num):
    num = int(hex_num, 16)
    ret = []

    for _ in range(4):
        ret.append(str(num % 2))
        num //= 2

    return ''.join(ret[-1:-5:-1])


T = int(input())
for tc in range(1, T + 1):
    N, hex_array = input().split()

    res = []
    for item in hex_array:
        res.extend(hex_to_bin(item))

    print(f'#{tc} {"".join(res)}')
