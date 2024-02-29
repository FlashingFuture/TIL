# 겹치는 부분이
# 직사각형 : a, 선분 : b, 점 : c, 겹치지 않음 : d
for tc in range(4):
    x_enough = False
    y_enough = False
    x_point = False
    y_point = False
    arr = list(map(int, input().split()))
    # 1. x축이 겹치는가
    if arr[0] < arr[4] < arr[2] or arr[0] < arr[6] < arr[2] or arr[4] < arr[0] < arr[6] or arr[4] < arr[2] < arr[6]:
        x_enough = True
    elif arr[0] == arr[4] or arr[2] == arr[6]:
        x_enough = True
    elif arr[2] == arr[4] or arr[0] == arr[6]:
        x_point = True

    # 2. y축이 겹치는가
    if arr[1] < arr[5] < arr[3] or arr[1] < arr[7] < arr[3] or arr[5] < arr[1] < arr[7] or arr[5] < arr[3] < arr[7]:
        y_enough = True
    elif arr[1] == arr[5] or arr[3] == arr[7]:
        y_enough = True
    elif arr[3] == arr[5] or arr[1] == arr[7]:
        y_point = True

    if x_enough and y_enough:
        print('a')

    elif (x_enough and y_point) or (x_point and y_enough):
        print('b')

    elif x_point and y_point:
        print('c')

    else:
        print('d')
