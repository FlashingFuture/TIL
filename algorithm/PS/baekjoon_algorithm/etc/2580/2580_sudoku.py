import sys
input = sys.stdin.readline


def check(y, x, n):
    for i in range(9):
        if plate[y][i] == n:    # 가로 확인
            return False
        
        if plate[i][x] == n:    # 세로 확인
            return False
    
    for i in range(3):          # 3x3 확인
        for j in range(3):
            if plate[(y // 3) * 3 + i][(x // 3) * 3 + j] == n:
                return False
                
    return True


plate = [list(map(int, input().split())) for _ in range(9)]
# 가능한 정답 케이스들을 스택에 넣은 후 dfs로 풀이
pos = []
for j in range(9):
    for i in range(9):
        if plate[j][i] == 0:
            pos.append((j, i))


def dfs(idx):
    if idx == len(pos):
        for i in range(9):
            print(*plate[i])

        exit(0)
    
    Y, X = pos[idx]
    for k in range(1, 10):
        if check(Y, X, k):
            plate[Y][X] = k
            dfs(idx + 1)
            plate[Y][X] = 0


dfs(0)