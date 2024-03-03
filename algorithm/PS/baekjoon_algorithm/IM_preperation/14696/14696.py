N = int(input())
# 별 / 동그라미 / 네모 / 세모 순으로 비교
for n in range(N):
    a = list(map(int, input().split()))     # a[0] : a의 원소의 개수
    b = list(map(int, input().split()))     # b[0] : b의 원소의 개수

    astar, acir, asq, atri = 0, 0, 0, 0
    bstar, bcir, bsq, btri = 0, 0, 0, 0  
    for i in range(1, a[0] + 1):
        if a[i] == 4:
            astar += 1
        
        elif a[i] == 3:
            acir += 1

        elif a[i] == 2:
            asq += 1

        elif a[i] == 1:
            atri += 1

    for i in range(1, b[0] + 1):
        if b[i] == 4:
            bstar += 1
        
        elif b[i] == 3:
            bcir += 1

        elif b[i] == 2:
            bsq += 1

        elif b[i] == 1:
            btri += 1


    if astar > bstar: print('A')
    elif astar < bstar: print('B')
    elif acir > bcir: print('A')
    elif acir < bcir: print('B')
    elif asq > bsq: print('A')
    elif asq < bsq: print('B')
    elif atri > btri: print('A')
    elif atri < btri: print('B')
    else: print('D')
    