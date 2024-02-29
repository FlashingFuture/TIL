def is_palindrome(array):
    for num in range(len(array) // 2):
        if array[num] != array[- num - 1]:
            return False

    return True


for tc in range(1, 11):  # 10번만큼 테스트 반복
    N = int(input())  # N : 찾아야 하는 회문의 길이
    arr = [input() for _ in range(8)]
    num_of_pal = 0  # 회문의 총 개수를 저장할 변수
    anum_of_pal = 0
    for i in range(8):
        for j in range(8 - N + 1):
            # 가로
            if is_palindrome(arr[i][j: j + N]):
                num_of_pal += 1

            temp = []  # 세로형태 문자를 받을 임시 배열
            for k in range(N):
                temp.append(arr[j + k][i])

            if is_palindrome(temp):
                num_of_pal += 1

    print(f'#{tc} {num_of_pal}')
