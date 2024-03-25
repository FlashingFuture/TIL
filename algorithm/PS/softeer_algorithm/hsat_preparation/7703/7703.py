import sys


N = int(sys.stdin.readline())
ans = []
for i in range(N):
    S, T = sys.stdin.readline().split()
    for idx in range(len(S)):
        if S[idx] == 'x' or S[idx] == 'X':
            ans.append(T[idx].upper())

print(''.join(ans))
