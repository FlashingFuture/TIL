def toggle(n):
    if arr[n] == 0:
        arr[n] = 1
    else:
        arr[n] = 0
    
    return n


n = int(input())    # num of switch
arr = [0] + list(map(int, input().split()))   # array of switch(첫 원소는 안쓰고 0으로 초기화)
s_num = int(input())  # num of students
for i in range(s_num):
    sex, num = map(int, input().split())
    # 남자인 경우
    if sex == 1:
        for j in range(1, n + 1):
            if j % num == 0:
                toggle(j)

    # 여자인 경우
    else:
        toggle(num)    # 기본 위치 토글
        for j in range(n // 2):
            if num + j > n or num - j < 1:
                break

            if arr[num + j] != arr[num - j]:
                break

            else:
                toggle(num + j)
                toggle(num - j)


# 출력
for i in range(1, n + 1):
    print(arr[i], end=' ')
    if i % 20 == 0:
        print()