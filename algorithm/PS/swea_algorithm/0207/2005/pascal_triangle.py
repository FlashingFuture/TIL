T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    print(f'#{tc}')     # tc 번호 출력

    temp = []
    for i in range(1, N + 1):
        arr = [1] * i
        for j in range(1, len(temp)):
            arr[j] = temp[j - 1] + temp[j]  # 아래 열에 사이값을 더해줌

        temp = arr
        print(*arr)     # 파스칼의 삼각형 한 줄씩 출력
