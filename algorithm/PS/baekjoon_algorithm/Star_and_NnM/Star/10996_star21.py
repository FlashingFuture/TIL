N = int(input())
if N == 1:
    print('*')
else:
    for i in range(N):
        arr1 = ['* ' * ((N + 1) // 2)]
        arr2 = [' *' * (N // 2)]
        print(''.join(arr1))
        print(''.join(arr2))