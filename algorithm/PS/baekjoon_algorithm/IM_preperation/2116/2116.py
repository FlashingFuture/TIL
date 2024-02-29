import copy

N = int(input())
dices = [[] for _ in range(N)]
for i in range(N):
    dices[i] = list(map(int, input().split()))
# 05 대칭, 13 대칭, 24 대칭

max_sum_list = []       # 각 면에서의 max_sum
for i in range(6):      # 여섯 면을 돌려가면서
    arr = copy.deepcopy(dices)
    temp = i                # temp에 선택한 주사위의 윗면의 인덱스 입력
    next_top = 0            # next_top 초기화
    max_list = []           # 옆면의 최댓값들을 저장할 리스트 초기화
    for j in range(N):
        if j:
            temp = arr[j].index(next_top)   # 2번째 주사위부터 윗면 인덱스 입력
        if temp == 0:
            arr[j].pop(0)     # 윗면 pop
            next_top = arr[j].pop(4)  # 아랫면 pop

        elif temp == 1:
            arr[j].pop(1)
            next_top = arr[j].pop(2)

        elif temp == 2:
            arr[j].pop(2)
            next_top = arr[j].pop(3)

        elif temp == 5:
            arr[j].pop(5)     # 윗면 pop
            next_top = arr[j].pop(0)  # 아랫면 pop

        elif temp == 3:
            arr[j].pop(3)
            next_top = arr[j].pop(1)

        elif temp == 4:
            arr[j].pop(4)
            next_top = arr[j].pop(2)

        max_list.append(max(arr[j]))    # 옆면 중 최댓값 append

    max_sum_list.append(sum(max_list))

print(max(max_sum_list))
