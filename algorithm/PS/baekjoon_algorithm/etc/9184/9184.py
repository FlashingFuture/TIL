def w(a, b, c):
    ww = [[[0] * 25 for _ in range(25)] for __ in range(25)]
    ww[0][0][0] = 1
    ww[0][0][-1] = 1
    ww[0][-1][0] = 1
    ww[-1][0][0] = 1
    ww[0][-1][-1] = 1
    ww[-1][0][-1] = 1
    ww[-1][-1][0] = 1
    ww[-1][-1][-1] = 1
    while a <= 20 and b <= 20 and c <= 20:




    return 0



while True:
    try:
        A, B, C = map(int, input().split())
    except EOFError:
        break

    res = w(A, B, C)
    print(f'w({A}, {B}, {C}) = {res}')