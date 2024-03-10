def z_search(n, y, x):
    if n == 0:
        return 0
    
    return 2 * (y % 2) + (x % 2) + 4 * z_search(n - 1, y // 2, x // 2)


N, r, c = map(int, input().split())
res = z_search(N, r, c)
print(res)
