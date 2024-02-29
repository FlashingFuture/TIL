n = int(input())
seq = []
for i in range(n): seq.append(int(input()))

stack = []
res = []
top = 1

for item in seq:
    while item >= top:
        stack.append(top)
        res.append('+')
        top += 1
    
    if stack[-1] == item:
        stack.pop()
        res.append('-')
    
    else:
        res = ['NO']
        break

for i in res:
    print(i)