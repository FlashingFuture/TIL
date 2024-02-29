pw_dict = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}


def pw_to_ans(bin_num):
    i = len(bin_num) - 1
    while i > 1:
        if bin_num[i] == '1':



T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    arr = list(set(arr))    # 중복 제거
    for item in arr:
        arr_bin = bin(int(item, 16))[2:].zfill(2)
        res = pw_to_ans(arr_bin)

    print(f'#{tc} {res}')