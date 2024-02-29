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


def pw_to_ans(char, n, m):
    ans = []
    for k in range(n):          # 각 층마다
        # 첫 암호의 위치 확인
        i = m
        end = 0
        while i > 1:
            i -= 1
            if char[k][i] == '1':
                end = i    # 종료 위치
                i = i - 55  # 시작 위치로 이동
                break

        while i < end:
            temp = char[k][i:i + 7]
            ans.append(pw_dict[temp])
            i += 7

        if ans:
            if ((ans[0] + ans[2] + ans[4] + ans[6]) * 3 + ans[1] + ans[3] + ans[5] + ans[7]) % 10 == 0:
                return sum(ans)
            else:
                return 0

    return 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    res = pw_to_ans(arr, N, M)
    print(f'#{tc} {res}')