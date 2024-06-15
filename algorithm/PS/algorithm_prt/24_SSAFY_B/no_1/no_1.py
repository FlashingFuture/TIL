def bitmask(test_case, number):
    bit_mask = 0b0000000000
    cnt = 1
    while True:
        for num in str(number * cnt):
            bit_mask = bit_mask | 1 << int(num)
            if bit_mask == 1023:
                print(f'#{test_case} {number * cnt}')
                return

        cnt += 1


T = int(input())
for tc in range(1, T + 1):
    bitmask(tc, int(input()))
