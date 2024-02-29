T = 4
plane = [[0]*100 for i in range(100)]

for t in range(T):
    square = list(map(int, input().split()))
    for i in range(square[0], square[2]):
        for j in range(square[1], square[3]):
            plane[i][j] = 1

total = 0
for i in range(100):
    for j in range(100):
        if plane[i][j] == 1:
            total += 1

print(total)
