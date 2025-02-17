import sys
from collections import deque


N = int(input())
A = list(map(int, sys.stdin.readline().split()))
# 맨 오른쪽에서부터 탐색하면서 스택에 값을 집어넣되
# 스택 안에서 해당 값보다 큰 값이 나오기 전까지 모든 값을 다 pop 해
# 효율적인 자료구조 사용
answer = deque([-1])
stack = [A[-1]]
for i in range(N - 2, -1, -1):
    value = A[i]
    while stack:
        # 1. 오큰수 찾기
        if stack[-1] > value:
            answer.appendleft(stack[-1])
            stack.append(value)
            break
        else:
            stack.pop()

    if not len(stack):
        answer.appendleft(-1)
        stack.append(value)

print(' '.join(map(str, list(answer))))