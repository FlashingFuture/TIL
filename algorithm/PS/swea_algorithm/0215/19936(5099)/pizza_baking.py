from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    temp = [[0, 0] for _ in range(N)]
    fire_pit = deque(temp)    # [0,0] 5개로 fire_pit 초기화
    k = 0
    while True:
        for i in range(N):
            if fire_pit[0][1] == 0:
                fire_pit.popleft()
                fire_pit.appendleft([k, C[k]])
                k += 1
                if k == M:
                    fire_pit.appendleft(fire_pit.pop())  # 큐 돌리기
                    fire_pit[0][1] //= 2  # 치즈 녹이기
                    break

            fire_pit.appendleft(fire_pit.pop())  # 큐 돌리기
            fire_pit[0][1] //= 2  # 치즈 녹이기

        if k == M:
            break

    # 마지막 5개 굽기(하나가 남을 때까지)
    while len(fire_pit) > 1:
        if fire_pit[0][1] == 0:
            fire_pit.popleft()

        fire_pit.appendleft(fire_pit.pop())
        fire_pit[0][1] //= 2

    result = fire_pit[0][0] + 1
    print(f'#{tc} {result}')