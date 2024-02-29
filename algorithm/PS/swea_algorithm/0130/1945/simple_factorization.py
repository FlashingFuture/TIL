# 테스트 케이스 개수 T 입력받음
T = int(input())
print(T)
# 테스트 케이스 반복하여 처리
for t in range(1, T + 1):
    # 숫자를 입력받음
    N = int(input())
    # 모든 지수 초기화
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    while N % 2 == 0:
        N /= 2
        a += 1

    while N % 3 == 0:
        N /= 3
        b += 1

    while N % 5 == 0:
        N /= 5
        c += 1

    while N % 7 == 0:
        N /= 7
        d += 1

    while N % 11 == 0:
        N /= 11
        e += 1

    print(f'#{t} {a} {b} {c} {d} {e}')