def find_ans(c, r, k):
    concert_hall = [[0] * c for _ in range(r)]
    res = 1
    count = 1
    pos = [r - 1, 0]
    while res <= r * c:
        for i in range(r - 2 * count + 1):
            concert_hall[pos[0]][pos[1]] = res
            if res == k: return pos[1] + 1, r - pos[0]
            res += 1
            pos[0] -= 1

        for i in range(c - 2 * count + 1):
            concert_hall[pos[0]][pos[1]] = res
            if res == k: return pos[1] + 1, r - pos[0]
            res += 1
            pos[1] += 1

        for i in range(r - 2 * count + 1):
            concert_hall[pos[0]][pos[1]] = res
            if res == k: return pos[1] + 1, r - pos[0]
            res += 1
            pos[0] += 1

        for i in range(c - 2 * count + 1):
            concert_hall[pos[0]][pos[1]] = res
            if res == k: return pos[1] + 1, r - pos[0]
            res += 1
            pos[1] -= 1

        pos[0] -= 1
        pos[1] += 1
        count += 1

    return [0]


C, R = map(int, input().split())
K = int(input())

ans = find_ans(C, R, K)
print(*ans)