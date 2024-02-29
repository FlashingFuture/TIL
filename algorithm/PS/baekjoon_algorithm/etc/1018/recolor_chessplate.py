def find_8x8(plate, dy, dx):
    cnt = 0
    for i in range(4):
        for j in range(4):
            if plate[2 * i + dy][2 * j + dx] == 'W':
                cnt += 1
            if plate[2 * i + dy][2 * j + 1 + dx] == 'B':
                cnt += 1
            if plate[2 * i + 1 + dy][2 * j + dx] == 'B':
                cnt += 1
            if plate[2 * i + 1 + dy][2 * j + 1 + dx] == 'W':
                cnt += 1
    
    if cnt > 32:
        cnt = 64 - cnt
    
    return cnt
            

N, M = map(int, input().split())
arr = [input() for _ in range(N)]

min_res = 1250
for i in range(N - 7):
    for j in range(M - 7):
        res = find_8x8(arr, i, j)
        if res < min_res:
            min_res = res

print(min_res)