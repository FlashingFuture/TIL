K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]

left = 1
right = max(arr)
while left <= right:
    div_num = (left + right) // 2

    cnt = 0
    for item in arr:
        cnt += item // div_num
    
    if cnt >= N:
        left = div_num + 1
    
    else:
        right = div_num - 1

print(right)