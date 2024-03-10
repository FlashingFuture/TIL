N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x:(x[1], x[0]))
s = 0
cnt = 0
for item in meetings:
    if s <= item[0]:
        s = item[1]
        cnt += 1

print(cnt)
