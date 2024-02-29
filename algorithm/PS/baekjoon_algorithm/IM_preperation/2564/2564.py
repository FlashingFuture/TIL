w, h = map(int, input().split())
n = int(input())
p_s = [[] for _ in range(n + 1)]    # position_shop
for i in range(n + 1):
    head, temp = map(int, input().split())
    if head == 1: p_s[i] = [1, temp, 0]
    elif head == 2: p_s[i] = [2, temp, h]
    elif head == 3: p_s[i] = [3, 0, temp]
    else: p_s[i] = [4, w, temp]

p_m = p_s[n]
# 구할 것
# 1. 자기 기준 옆면으로의 순수 위치차이
# 2. 자기 기준 같은 방향과의 순수 위치차이
# 3. 자기 기준 반대편과의 총 거리차이 : 전체 둘레의 반 - (축대칭위치와의 순수 위치차이)
# 반대편 미리 구해놓기
ops = -1
if p_m[0] == 2: ops = 1
elif p_m[0] == 1: ops = 2
elif p_m[0] == 4: ops = 3
elif p_m[0] == 3: ops = 4

res = 0
for item in p_s:
    if item[0] == ops:
        if ops <= 2:    # 남북 대칭일경우
            temp = item[1] + p_m[1]
            if temp > w:
                res += (h + (w - item[1]) + (w - p_m[1]))
            else:
                res += (h + item[1] + p_m[1])
        else:           # 동서 대칭일경우
            temp = item[2] + p_m[2]
            if temp > h:
                res += (w + (h - item[2] + h - p_m[2]))
            else:
                res += (w + item[2] + p_m[2])
    else:
        res += (abs(item[1] - p_m[1]) + abs(item[2] - p_m[2]))

print(res)

