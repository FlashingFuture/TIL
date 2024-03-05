# n개의 퀸을 놓으려면 각 줄마다 하나씩만 놓아야 한다
path = []


def backtrack(n):
    if n == N:
        global cnt
        cnt += 1
        return

    for i in range(N):      # 왼쪽 대각, 위, 오른쪽 대각에 겹치는 부분이 없다면 append(i)
        if i in path: continue      # 위가 겹친다면 continue
        cont = False
        for j in range(1, n + 1):
            # 왼쪽 위
            if path[n - j] == i - j:
                cont = True
                break

        if cont: continue
        for j in range(1, n + 1):
            # 오른쪽 위
            if path[n - j] == i + j:
                cont = True
                break

        if cont: continue
        path.append(i)
        backtrack(n+1)
        path.pop()


N = int(input())
cnt = 0
backtrack(0)
print(cnt)
