for tc in range(1, 11):
    N, arr = input().split()  # N, arr을 문자열 형태로 받아옴

    char_list = []
    for i in range(int(N)):
        char_list.append(arr[i])  # arr packing to char_list

    i = 0
    while i < len(char_list) - 1:
        if char_list[i] == char_list[i + 1]:    # 앞뒤 숫자가 같을시
            char_list.pop(i)    # 그 두
            char_list.pop(i)    # 수를 리스트에서 빼버리고
            i -= 1      # 한 칸 전으로 이동
        else:
            i += 1

    ans = ''.join(char_list)
    print(f'#{tc} {ans}')
