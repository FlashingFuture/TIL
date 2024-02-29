import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())

p_st = deque([2])  # 소수 스택 : 1은 소수가 아니므로 2부터 시작
for i in range(2, N + 1):
    is_prime = True
    for p_num in p_st: 
        if p_num > int(N**0.5 + 1):
            break
        if i % p_num == 0:
            is_prime = False
            break
        
    if is_prime == True:
        p_st.append(i)

need_pop = 0
for item in p_st:     # M보다 작은 소수 스택에서 빼기
    if item < M:
        need_pop += 1
    else:
        break

for i in range(need_pop):
    p_st.popleft()

if N == 1:
    p_st.popleft()

for item in p_st:
    print(item)