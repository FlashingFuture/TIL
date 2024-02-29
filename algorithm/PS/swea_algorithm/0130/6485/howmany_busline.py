# 테스트 케이스의 개수 T 입력받음
T = int(input())
# T만큼 테스트 케이스를 반복 처리
for t in range(1, T + 1):
    # 버스 노선의 개수 N 입력받음
    N = int(input()) # 버스 노선의 개수
    a = [0] * N
    b = [0] * N
    # n줄 동안 a, b,에 정수를 입력받음
    for n in range(N):
        a[n], b[n] = map(int, input().split())
    # 정수 P를 입력받음
    P = int(input())
    c = [0] * P

    print(f'#{t}', end=" ")

    for p in range(P):
        num_of_bus = 0
        c[p] = int(input())
        for n in range(N):
            if a[n] <= c[p] <= b[n]:
                num_of_bus += 1

        print(num_of_bus, end=" ")

    print()
