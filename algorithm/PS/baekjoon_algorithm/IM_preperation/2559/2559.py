N, K = map(int, input().split())    # N : 전체 날짜 K : K일간의 합 구함
lst = list(map(int, input().split()))

temp_lst = []
sum_lst = []                        # K일간 온도의 합들을 저장할 리스트
for i in range(K):
    temp_lst.append(lst[i])         # 임시 리스트에 1~K일의 온도 저장

sum_lst.append(sum(temp_lst))       # 1~K일 온도의 합을 리스트에 append

for i in range(1, N - K + 1):          # pop, append를 활용해 큐처럼 temp_lst 이용
    temp_lst.append(lst[i + K - 1])
    sum_lst.append(sum_lst[i - 1] + temp_lst[K] - temp_lst.pop(0))

print(max(sum_lst))