from collections import deque


for tc in range(1, 11):
    __ = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    no_zero_arr = [deque() for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if arr[j][i] != 0:
                no_zero_arr[i].append(arr[j][i])

    cnt = 0
    for item in no_zero_arr:
        # 1은 아래로, 2는 위로 민다
        while item:  # 정방향 : 2 위로 밀기
            if item[0] == 2:
                item.popleft()
            else:
                break

        while item:     # 역방향 : 1 아래로 밀기
            if item[-1] == 1:
                item.pop()
            else:
                break

        for i in range(len(item) - 1):      # 교합 세기
            if item[i] == 1 and item[i + 1] == 2:
                cnt += 1

    print(f'#{tc} {cnt}')

