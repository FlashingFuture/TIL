T = int(input())
# K : 1충으로 갈 수 있는 최대 정류장
# N : 종점
# M : 충전기가 설치된 정류장 개수
for t in range(1, T + 1):
    K, N, M = map(int, input().split())
    M_num = list(map(int, input().split()))

    # 다음 충전 정류장까지의 거리보다 K가 작은 경우 0을 출력
    # 최대 거리를 간 후, 1씩 줄여가면서 충전장을 검색하는 방식
    position = 0
    charge_num = 0
    for i in range(M + 1):
        # 최대 거리 이동
        position += K
        # 종점일 경우 break
        if position >= N:
            break

        for j in range(K, 0, -1):
            # 충전장 검색
            if position in M_num:
                charge_num += 1
                break
            # 1을 줄인 후 재탐색
            position -= 1

    # 도착하지 못한 경우 charge_num에 0을 할당
    if position < N:
        charge_num = 0

    print(f'#{t} {charge_num}')
