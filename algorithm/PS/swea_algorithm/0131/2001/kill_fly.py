T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split()) # 전체 배열의 크기 N. 파리채의 길이/높이 M
    arr = [] # 전체 배열
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    best_kill_score = 0 # 최대 파리 스코어

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            kill_score = 0
            for k in range(M):
                for l in range(M):
                    kill_score += arr[i + k][j + l]

            if kill_score > best_kill_score:
                best_kill_score = kill_score

    print(f'#{t} {best_kill_score}')
