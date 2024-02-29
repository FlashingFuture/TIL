def is_palindrome(array):
    for num in range(len(array) // 2):
        if array[num] != array[- num - 1]:
            return False

    return True


T = int(input())
for tc in range(1, T + 1):      # T만큼 테스트 케이스 반복
    N, M = map(int, input().split())    # 글자판의 사이즈 N, 회문의 길이 M
    arr = [str(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N - M + 1):
            if is_palindrome(arr[i][j: j + M]):
                print(f'#{tc} {arr[i][j: j + M]}')

            temp = []
            for k in range(M):
                temp.append(arr[j + k][i])

            temp = ''.join(temp)
            if is_palindrome(temp):
                print(f'#{tc} {temp}')
