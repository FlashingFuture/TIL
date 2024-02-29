T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    dict_str2 = {}                  # str2의 각 값의 개수를 저장할 dict

    for item in str2:               # dict에 값을 넣고 각 개수만큼 값을 할당
        try:
            dict_str2[item] += 1
        except KeyError:
            dict_str2[item] = 1

    ans = 0
    for item in str1:               # 최댓값 찾기
        if item in dict_str2:
            if ans < dict_str2[item]:
                ans = dict_str2[item]

    print(f'#{tc} {ans}')
