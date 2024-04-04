from collections import deque


N = int(input())
f_l_line = ['*'] * N
for _ in range(2*N - 3):
    f_l_line.append(' ')
for _ in range(N):
    f_l_line.append('*')

print(''.join(f_l_line))
for i in range(1, N):
    line = [' '] * i
    line.append('*')
    for _ in range(N - 2):
        line.append(' ')
    line.append('*')
    for _ in range(N - 1 - i):
        line.append(' ')

    if i != N - 1:
        for _ in range(N - 2 - i):
            line.append(' ')
        line.append('*')
    for _ in range(N - 2):
        line.append(' ')
    line.append('*')
    print(''.join(line))

for i in range(N - 1, 0, -1):
    line = [' '] * i
    line.append('*')
    for _ in range(N - 2):
        line.append(' ')
    line.append('*')
    for _ in range(N - 1 - i):
        line.append(' ')

    if i != N - 1:
        for _ in range(N - 2 - i):
            line.append(' ')
        line.append('*')
    for _ in range(N - 2):
        line.append(' ')
    line.append('*')
    print(''.join(line))

print(''.join(f_l_line))