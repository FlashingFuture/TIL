T = 10
# 테스트 케이스의 개수 T만큼 반복하여 처리
for t in range(1, T + 1):
    _ = int(input())     # 테스트 케이스 번호를 받기만 함
    # 100 X 100 배열을 입력받음
    arr = []
    for i in range(100):
        line = list(map(int, input().split()))
        arr.append(line)

    sum_list = [] # 가로 / 세로 / 대각선을 더한 값을 모을 리스트
    for i in range(100):
        column = 0
        row = 0
        for j in range(100):
            column += arr[i][j]
            row += arr[j][i]

        sum_list.append(column)
        sum_list.append(row)

    diagonal = 0
    diagonal_reverse = 0
    for i in range(100):
        diagonal += arr[i][i]
        diagonal_reverse += arr[i][99 - i]

    sum_list.append(diagonal)
    sum_list.append(diagonal_reverse)

    print(f'#{t} {max(sum_list)}')