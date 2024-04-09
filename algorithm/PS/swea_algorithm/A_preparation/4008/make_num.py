from collections import deque


# 0 = plus, 1 = minus, 2 = multi, 3 = divide 로 path에 넣으며 백트래킹
path = []


def backtrack(lev):
    if lev == N - 1:
        print(path)
        temp_nums = deque([nums[x] for x in range(N)])  # popleft를 위해 deque
        temp = temp_nums.popleft()
        for op in path:     # for operators in path
            if op == 0:
                temp += temp_nums.popleft()
            elif op == 1:
                temp -= temp_nums.popleft()
            elif op == 2:
                temp *= temp_nums.popleft()
            elif op == 3:
                if temp < 0:
                    temp = -temp
                    temp //= temp_nums.popleft()
                    temp = -temp
                else:
                    temp //= temp_nums.popleft()

        global max_num, min_num
        max_num = max(max_num, temp)
        min_num = min(min_num, temp)
        return

    if path.count(0) < plus:
        path.append(0)
        backtrack(lev + 1)
        path.pop()

    if path.count(1) < minus:
        path.append(1)
        backtrack(lev + 1)
        path.pop()

    if path.count(2) < multi:
        path.append(2)
        backtrack(lev + 1)
        path.pop()

    if path.count(3) < divide:
        path.append(3)
        backtrack(lev + 1)
        path.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    plus, minus, multi, divide = map(int, input().split())
    nums = list(map(int, input().split()))
    max_num = -999999999999
    min_num = 999999999999

    backtrack(0)
    res = max_num - min_num
    print(f'#{tc} {res}')