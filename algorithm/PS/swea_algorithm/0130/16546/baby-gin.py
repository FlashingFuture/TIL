def baby_gin(card_str):
    '''
    6장의 카드가
    run(3장의 카드번호가 연속적임) triple(3장의 카드번호가 같음)으로만 이뤄져야
    True를 반환, 아니라면 False를 반환하는 함수
    counting sort를 통해 함수를 구성
    '''
    count = [0] * 10
    # 수 카운팅
    for i in card_str:
        count[int(i)] += 1

    # 트리플 여부 확인 및 run_or_triple counter 선언
    run_or_triple = 0
    temp = 0
    while temp < 10:
        # 트리플일 시 count에서 값을 빼내고 카운터 값을 올림
        if count[temp] >= 3:
            run_or_triple += 1
            count[temp] -= 3
            continue

        temp += 1
    # check run later
    temp = 0
    while temp < 8:
        # 런일 시 count에서 값을 빼내고 카운터 값을 올림
        if count[temp] >= 1 and count[temp + 1] >= 1 and + count[temp + 2] >= 1:
            count[temp] -= 1
            count[temp + 1] -= 1
            count[temp + 2] -= 1
            run_or_triple += 1
            continue

        temp += 1

    return run_or_triple == 2

# 테스트케이스의 개수 T 입력받음
T = int(input())
# T번만큼 반복하여 처리
for t in range(1, T + 1):
    # card_str에 6자리 숫자를 문자열로써 저장
    card_str = str(input())
    # card_str을 baby_gin에 넣은 후 출력
    result = baby_gin(card_str)
    print(f'#{t} {result}')