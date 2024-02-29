T = int(input())
for tc in range(1, T + 1):  # T만큼 테스트 케이스 반복
    T, N = map(str, input().split())
    arr = list(map(str, input().split()))
    alien_num = ["ZRO", "ONE", "TWO", "THR", "FOR",
                 "FIV", "SIX", "SVN", "EGT", "NIN"]  # 번역기
    count_list = [0] * 10       # count값을 저장할 리스트
    for item in arr:
        count_list[alien_num.index(item)] += 1

    print(T)
    result = []
    for i in range(10):
        for j in range(count_list[i]):
            result.append(alien_num[i])

    print(*result)
