# 테스트 케이스 10건이 주어짐
T = 10
# 테스트 케이스 각각을 처리
for t in range(1, T + 1):
    dump_num = int(input())
    arr = list(map(int, input().split()))
    # 1. 완전 탐색으로 우선 풀어보기
    # dump_num만큼 반복
    for i in range(dump_num):
        # 가로 0~99을 순회하면서 최대 / 최소값을 얻어 최대에서 1을 깎고 최소에 1을 더해줌
        # min_h / max_h 초기화
        min_h = 100
        max_h = 0
        # 최고 / 최저점의 높이 저장소 초기화
        temp_highest = 0
        temp_lowest = 0
        for j in range(100):
            if arr[j] > max_h:
                max_h = arr[j]
                temp_highest = j

            if arr[j] < min_h:
                min_h = arr[j]
                temp_lowest = j

        # dump 실행
        arr[temp_highest] -= 1
        arr[temp_lowest] += 1

    min_h = 100
    max_h = 0

    for i in range(100):
        if arr[i] > max_h:
            max_h = arr[i]

        if arr[i] < min_h:
            min_h = arr[i]

    print(f'#{t} {max_h - min_h}')
