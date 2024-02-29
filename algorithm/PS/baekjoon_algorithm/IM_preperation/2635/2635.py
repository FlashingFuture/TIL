def recursive_minus(num):
    max_cnt = 0     # 결과 출력값
    max_list = []   # 결과 출력 리스트
    for i in range(1, num + 1):
        cnt = 2
        temp_list = []
        temp_list.append(num)   # 배열에 num 추가
        temp_list.append(i)     # 배열에 i(처음 빼는 값) 추가
        while True:             # while temp_list[cnt] < [cnt - 1]
            next_num = temp_list[cnt - 2] - temp_list[cnt - 1]
            if next_num < 0:
                break

            cnt += 1
            temp_list.append(next_num)

        if max_cnt < cnt:
            max_cnt = cnt
            max_list = temp_list

    print(max_cnt)
    for i in range(max_cnt):
        print(max_list[i], end=' ')


num = int(input())
recursive_minus(num)


        


    