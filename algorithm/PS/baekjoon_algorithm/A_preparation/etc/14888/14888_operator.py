from collections import deque


path = []


def backtrack(n):
    if n == (N - 1):
        a = deque([A[x] for x in range(len(A))])
        global max_num
        global min_num
        for item in path:
            if item == 0:       # +
                a.appendleft(a.popleft() + a.popleft())

            elif item == 1:     # -
                temp = a.popleft()
                a.appendleft(temp - a.popleft())

            elif item == 2:     # *
                a.appendleft(a.popleft() * a.popleft())

            elif item == 3:     # //
                temp = a.popleft()
                if temp < 0:
                    temp = (-temp) // a.popleft()
                    a.appendleft(-temp)
                else:
                    a.appendleft(temp // a.popleft())

        if a[0] > max_num:
            max_num = a[0]

        if a[0] < min_num:
            min_num = a[0]

        return

    for i in range(4):
        if path.count(i) == ops[i]: continue
        path.append(i)
        backtrack(n + 1)
        path.pop()


N = int(input())
A = deque(list(map(int, input().split())))
ops = list(map(int, input().split()))   # ops[0]:+, [1]:-, [2]:*, [3]://
# 4개 부호를 개수만큼 조합
max_num = -1000000000
min_num = 1000000000
backtrack(0)
print(max_num)
print(min_num)
