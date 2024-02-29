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


def pw_to_ans(code, cnt):
    start_point = []    # 시작 위치를 저장할 카운터
    sum_of_code = 0     # 총합을 저장할 변수
    i = 56*cnt + 4
    end = 0
    while i > 1:
        i -= 1
        if code[i] == '1':
            end = i    # 종료 위치
            i = i - 55  # 시작 위치로 이동
            start_point.append(i)

    for i in start_point:
        ans = []
        while i < end:
            one_code = ''
            for j in range(7):
                one_code += code[i + j*cnt]

            ans.append(pw_dict[one_code])
            i += 7

        if ans:
            if ((ans[0] + ans[2] + ans[4] + ans[6]) * 3 + ans[1] + ans[3] + ans[5] + ans[7]) % 10 == 0:
                sum_of_code += sum(ans)

    return sum_of_code


def find_and_decode(char, n, m):
    # 0이 아닌 점 뒤에서부터 찾기
    code_start = []  # 암호의 시작점들을 담을 list
    sum_of_ans = 0      # 답을 더해줄 변수
    for i in range(n):
        point = m - 1
        while point > 1:
            cnt = 0
            if char[i][point] != '0':
                while char[i][point - 1] != '0':   # 암호의 시작점을 찾을 때까지
                    point -= 14
                    cnt += 1
                if point not in code_start:
                    code_start.append(point)
                    # print(bin_code)
                    temp = bin(int(char[i][point:point + 14*cnt + 1], 16))[2:].zfill(56*cnt + 4)
                    is_pw = pw_to_ans(temp, cnt)
                    sum_of_ans += is_pw

                    point += 1

            point -= 1

    return sum_of_ans


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    res = find_and_decode(arr, N, M)
    print(f'#{tc} {res}')