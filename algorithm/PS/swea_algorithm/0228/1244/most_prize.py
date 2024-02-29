def exchange(n):
    if n == int(N):
        global max_prize
        if int(''.join(IC)) > max_prize:
            max_prize = int(''.join(IC))
        return

    for k in range(len(C) - 1):
        for L in range(k + 1, len(C)):
            IC[k], IC[L] = IC[L], IC[k]
            if (IC, n) not in visited_case:
                visited_case.append(([IC[x] for x in range(len(C))], n))
                exchange(n + 1)
            IC[k], IC[L] = IC[L], IC[k]


T = int(input())
for tc in range(1, T + 1):
    C, N = input().split()
    IC = list(C)      # char to list
    max_prize = -1
    visited_case = []
    exchange(0)
    print(f'#{tc} {max_prize}')
