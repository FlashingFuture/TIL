N = int(input())

cnt = 0
for i in range(5000000):
    n_six = 0
    temp = i
    while temp:
        if temp % 10 == 6:
            n_six += 1
        else:
            n_six = 0

        if n_six >= 3:
            n_six = 0
            cnt += 1
            break

        temp //= 10

    if N == cnt:
        print(i)
        break
