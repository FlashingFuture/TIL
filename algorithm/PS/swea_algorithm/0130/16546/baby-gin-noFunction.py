# 테스트케이스의 개수 T 입력받음
T = int(input())
# T번만큼 반복하여 처리
for t in range(1, T + 1):
    # 6개의 카드 input
    card = int(input())
    # count할 배열 선언
    count = [0] * 12
    for i in range(6):
        count[card % 10] += 1
        card //= 10

    temp = 0
    # triple / run 성공 시 올라갈 counter
    counter = 0
    while temp < 10:
        # triple을 먼저 확인
        if count[temp] >= 3:
            count[temp] -= 3
            counter += 1
            continue
        # run을 확인
        if count[temp] >= 1 and count[temp + 1] >= 1 and count[temp + 2] >= 1:
            count[temp] -= 1
            count[temp + 1] -= 1
            count[temp + 2] -= 1
            counter += 1
            continue

        temp += 1

    if counter == 2:
        print(f'#{t} true')
    else:
        print(f'#{t} false')