def ladder_down(arr):
    first_line = list(map(int, arr[0]))  # 사다리의 맨 윗 줄
    start = []
    for i in range(100):
        if first_line[i] == 1:
            start.append(i)     # 맨 윗줄이 1인 위치만 start에 저장

    for i in range(len(start)):
        x = start[i]    # x 좌표
        for j in range(100):

            if x != 0 and arr[j][x - 1] == 1:  # 왼쪽으로 이동
                while x != 0 and arr[j][x - 1] == 1:
                    x -= 1

            elif x != 99 and arr[j][x + 1] == 1:  # 오른쪽으로 이동
                while x != 99 and arr[j][x + 1] == 1:
                    x += 1

        if arr[99][x] == 2:
            return start[i]

    return False


T = 10
for tc in range(1, T + 1):
    _ = int(input()) # 테스트 케이스 번호를 받기만 함
    arr = [list(map(int, input().split())) for i in range(100)]
    print(f'#{tc} {ladder_down(arr)}')

