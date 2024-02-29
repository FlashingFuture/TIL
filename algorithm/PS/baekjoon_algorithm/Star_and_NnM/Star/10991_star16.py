N = int(input())
arr = [' ' * (N - 1), '*']
print(''.join(arr))
for i in range(1, N - 1):
    arr = [(' ' * (N - i - 1)), '*',  '  ' * (i - 1), ' *']
    print(''.join(arr))

if N >= 2:
    arr = ['*' * (2 * N - 1)]
    print(''.join(arr))