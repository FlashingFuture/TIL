T = int(input())
for tc in range(1, T + 1):
    # 각 학생이 복도를 전부 지나간다면 필연적으로 가장 많이 다니는 점 존재
    # 그 점을 매 횟수 지나간다면 최단 시간 안에 모든 학생이 자신의 방으로 돌아감
    N = int(input())
    cor_cnt = [0] * 200         # corridor counter
    for _ in range(N):
        st_room, end_room = map(int, input().split())
        st, end = (st_room - 1) // 2, (end_room - 1) // 2   # 실제로 지나가는 복도의 위치
        if st > end:
            st, end = end, st
        for i in range(st, end + 1):
            cor_cnt[i] += 1

    result = max(cor_cnt)
    print(f'#{tc} {result}')
