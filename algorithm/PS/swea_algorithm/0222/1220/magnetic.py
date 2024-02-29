for tc in range(1, 11):
    ____ = int(input())    # 100
    table = [list(map(int, input().split())) for _ in range(100)]
    deadlock_cnt = 0
    for i in range(100):
        for j in range(100):
            if table[i][j] == 2:    # s극 위로 떨구기
                for k in range(i - 1, -1, -1):  # 위를 하나하나 확인하면서
                    if table[k][j] == 1:
                        break
                    elif table[k][j] == 2:
                        break

                else:   # for k 동안 막히지 않았다면
                    table[i][j] = 0         # 테이블에서 없앰

    for i in range(100):
        for j in range(100):
            if table[99 - i][j] == 1:          # n극 아래로 떨구기
                for k in range(100 - i, 100):     # 아래를 하나하나 확인하면서
                    if table[k][j] == 2:
                        deadlock_cnt += 1           # deadlock 확인 시 cnt++
                        break
                    elif table[k][j] == 1:
                        break

                else:   # for k 동안 막히지 않았다면
                    table[99 - i][j] = 0

    print(f'#{tc} {deadlock_cnt}')