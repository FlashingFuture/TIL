T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    # 트럭은 하나만 옮길 수 있기에, 화물을 무게 순으로 정렬해 하나씩 트럭에 넣는다
    w.sort()
    t.sort()
    total_w = 0
    while w and t:      # 트럭, 화물이 둘 다 남은 동안:
        temp = w.pop()      # 화물을 꺼냄
        if t[-1] >= temp:
            t.pop()
            total_w += temp

    print(f'#{tc} {total_w}')
