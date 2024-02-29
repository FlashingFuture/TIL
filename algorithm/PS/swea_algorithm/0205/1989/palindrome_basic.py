T = int(input())
for tc in range(1, T + 1):
    L = str(input()).strip()
    truth = 1
    for i in range(len(L)):
        if L[i] != L[- i - 1]:
            truth = 0
            break

    print(f'#{tc} {truth}')