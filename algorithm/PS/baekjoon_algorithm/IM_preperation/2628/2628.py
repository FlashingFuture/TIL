C, R = map(int, input().split())    # Row, Column value
N = int(input())                    # number of lines
R_cut = []
C_cut = []
for _ in range(N):
    A, B = map(int, input().split())   # info of line
    if A == 0:
        R_cut.append(B)
    else:
        C_cut.append(B)

R_cut.append(R)
C_cut.append(C)

R_cut.sort()
C_cut.sort()

R_len = []
C_len = []
R_len.append(R_cut[0])
C_len.append(C_cut[0])

for i in range(1, len(R_cut)):
    R_len.append(R_cut[i] - R_cut[i - 1])

for i in range(1, len(C_cut)):
    C_len.append(C_cut[i] - C_cut[i - 1])
    
area = []

for i in R_len:
    for j in C_len:
        area.append(i * j)


print(max(area))