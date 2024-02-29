T = int(input())
for tc in range(1, T + 1):  # T만큼 테스트 반복
    str1 = str(input())
    str2 = str(input())

    result = 0
    for i in range(len(str2) - len(str1) + 1):
        temp = 0
        for j in range(len(str1)):
            if str1[j] != str2[i + j]:
                break

            temp += 1

        if temp == len(str1):
            result = 1

    print(f'#{tc} {result}')
