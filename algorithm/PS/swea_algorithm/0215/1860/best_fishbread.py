def selling_bread(m, k, arr):
    arr.sort()
    bread_left = 0  # 남은 빵의 수
    temp = 0
    leftover_time = 0       # 완성을 못했지만 굽던 시간
    for item in arr:
        temp = item - temp      # 이전 방문 시간과 현 방문 시간의 차이
        bread_left += (temp // m) * k   # 그 시간동안 구운 붕어빵 추가
        leftover_time += temp % m
        if leftover_time >= m:          # 이전 횟수로부터 물려받은 시간을 더해 한 번 더 구웠을 시
            leftover_time -= m
            bread_left += k

        bread_left -= 1         # 붕어빵 판매
        if bread_left < 0:      # 붕어빵이 없다면
            return 'Impossible'

        temp = item             # temp에 이전 방문시간 넣음

    return 'Possible'


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # N : 손님의 수 / M : 걸리는 시간 / K : 한번에 나오는 붕어빵
    arrival_time = list(map(int, input().split()))
    res = selling_bread(M, K, arrival_time)
    print(f'#{tc} {res}')

