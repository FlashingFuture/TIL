N = int(input())
chessboard = [[0] * N for _ in range(N)]


def backtrack(n, y, x):
    if n == N:
        global cnt
        cnt += 1
        return

    for i in range(x + 1, N):       # 같은 줄의 오른쪽 찾기
        chessboard
        backtrack(n + 1, y, i)

    for i in range(y + 1, N):       # 아랫줄 전부 찾기
        for j in range(N):
            backtrack(n + 1, i, j)


cnt = 0
backtrack(0, 0, 0)
print(cnt)