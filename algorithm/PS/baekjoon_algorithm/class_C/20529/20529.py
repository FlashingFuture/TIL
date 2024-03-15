from itertools import permutations


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(input().split())

    MBTI_dict = {}
    for item in arr:
        if item not in MBTI_dict:
            MBTI_dict[item] = 1
        else:
            MBTI_dict[item] += 1

    if max(MBTI_dict.values()) >= 3:
        print(0)

    else:
        temp_list = []
        for key, value in MBTI_dict.items():
            for i in range(value):
                temp_list.append(key)

        data = permutations(temp_list, 3)
        min_sum = 10
        for case in data:
            temp = 0
            for i in range(4):
                if case[0][i] != case[1][i]:
                    temp += 1
                if case[0][i] != case[2][i]:
                    temp += 1
                if case[1][i] != case[2][i]:
                    temp += 1

            if min_sum > temp:
                min_sum = temp

        print(min_sum)
