T = int(input())
for t in range(1, T + 1):
    # 카드의 장수 N
    N = int(input())
    card = int(input())
    # 개수를 저장할 count 배열 선언
    count = [0] * 10
    for i in range(N):
        count[card % 10] += 1
        card //= 10

    # 위로부터 count 배열을 순회하여 최빈값 추출(같을 경우 가장 큰 카드)
    the_num = 0
    # 최빈 카드값을 저장할 변수 선언
    the_card = 0
    for i in range(9, -1, -1):
        if count[i] > the_num:
            the_num = count[i]
            the_card = i

    print(f'#{t} {the_card} {the_num}')
