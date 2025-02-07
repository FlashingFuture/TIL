def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    # 입력 처리
    N, B = int(data[0]), int(data[1])
    f = [0] + list(map(int, data[2:N + 2]))  # 타일 눈 깊이, 1-based index로 맞춤
    s = [0] * (B + 1)
    d = [0] * (B + 1)
    idx = N + 2
    for j in range(1, B + 1):
        s[j], d[j] = map(int, data[idx:idx + 2])
        idx += 2

    # t 배열 초기화
    t = [False] * (N + 1)
    t[1] = True  # 첫 타일은 항상 도달 가능

    # 부츠 탐색
    for j in range(1, B + 1):
        for i in range(1, N + 1):
            if s[j] >= f[i]:  # 부츠 j가 타일 i에서 착용 가능하다면
                able = False
                for k in range(1, d[j] + 1):
                    if i - k >= 1 and t[i - k] and s[j] >= f[i - k]:
                        able = True
                        break
                t[i] |= able

        # 마지막 타일(N)에 도달 가능하면 종료
        if t[N]:
            print(j - 1)
            return


if __name__ == "__main__":
    main()