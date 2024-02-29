N = int(input())

arr = []
arr.append(' ' * (N - 1))
arr.append('*')
print(''.join(arr))

for i in range(1, N):
    arr = []
    for j in range(1, N - i):
        arr.append(' ')
    arr.append('*')
    arr.append(' ' * (2 * i - 1))
    arr.append('*')

    print(''.join(arr))