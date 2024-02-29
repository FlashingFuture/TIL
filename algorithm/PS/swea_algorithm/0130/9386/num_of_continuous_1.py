# 테스트 케이스 개수 T
T = int(input())
# 테스트 케이스를 반복하여 처리
for t in range(1, T + 1):
    # 수열의 길이 N을 입력받음
    N = int(input())
    # 길이 N의 2진 수열 입력받음
    arr = str(input())
    # 연속한 1의 개수의 최댓값 구하기
    # 수열 전체에서 반복(완전탐색)
    # counting을 통해 구함: count 배열 선언
    count = [0] * N
    j = 0
    for i in range(N):
        # arr[i]가 1이 나오면 0이 나올때까지 count의 한 칸에 값을 더함
        if arr[i] == '1':
            count[j] += 1
        # arr[i]가 0이 나오고 현재 카운트에 값이 있으면 다음 카운트로 넘김
        elif count[j] != 0:
            j += 1
    # max_num에 count의 최댓값 저장
    max_num = 0
    for item in count:
        if item > max_num:
            max_num = item
    # 출력
    print(f'#{t} {max_num}')