from collections import deque

arr = [list(map(int, input().split())) for _ in range(5)]
call = deque()
for _ in range(5):
    temp = list(map(int, input().split()))
    for i in range(5):
        call.append(temp[i])

ans_sheet = [[0] * 5 for _ in range(5)]
# 빙고를 위해 필요한 최소 입력은 12개므로 우선 11개를 입력받아 정답지에 기록
for _ in range(11):
    num = call.popleft()
    for i in range(5):
        for j in range(5):
            if arr[i][j] == num:
                ans_sheet[i][j] = 1

case_cnt = 11
while True:     # 빙고가 나올 때까지
    case_cnt += 1
    num = call.popleft()
    for i in range(5):
        for j in range(5):
            if arr[i][j] == num:
                ans_sheet[i][j] = 1

    bingo_cnt = 0
    for i in range(5):      # 빙고 확인
        if arr[i][0]:       # 가로 확인
            for j in range(5):
                if ans_sheet[i][j] == 0:
                    break

            else:   # for j
                bingo_cnt += 1

        if arr[0][i]:       # 세로 확인
            for j in range(5):
                if ans_sheet[j][i] == 0:
                    break

            else:   # for j
                bingo_cnt += 1

    for i in range(5):      # 좌하향 대각선 확인
        if ans_sheet[i][i] == 0:
            break

    else:   # for i
        bingo_cnt += 1

    for i in range(5):      # 우하향 대각선 확인
        if ans_sheet[i][4 - i] == 0:
            break

    else:   # for i
        bingo_cnt += 1

    if bingo_cnt >= 3:
        break

print(case_cnt)
