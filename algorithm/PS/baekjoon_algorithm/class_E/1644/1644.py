N = int(input())
# 소수로만 더해 나가면서 제일 큰 값이 4백만을 넘기면 그만두면 되는 문제
# 우선 1~N 사이의 소수를 구해야 함
# 완전탐색으로 구하면 당연히 시간초과므로 DP를 활용
prime_list = [True] * (N + 1)
prime_list[0] = False
prime_list[1] = False
prime_numbers = []
for i in range(2, N + 1):
    if prime_list[i]:
        prime_numbers.append(i)
        for j in range(2*i, N + 1, i):
            prime_list[j] = False

# 이제 소수 숫자들이 담긴 prime_numbers 리스트를 순회하여 소수의 합의 경우의수를 찾아야함
# 이 역시 완전탐색으로 찾기에는 리스트가 길기 때문에 투 포인터로 풀이
sum_of_num = 0
j = 0
ans_count = 0
for i in range(len(prime_numbers)):
    # 우선 다음 위치의 소수값을 더해주고
    sum_of_num += prime_numbers[i]
    if sum_of_num > N:      # 합이 N 을 넘어간 경우
        while sum_of_num > N:   # 합이 N 보다 작거나 같아질 때까지 왼쪽 포인터를 옮김
            sum_of_num -= prime_numbers[j]
            j += 1

    if sum_of_num == N:     # 연속된 소수의 합으로 나타난 경우
        ans_count += 1
        sum_of_num -= prime_numbers[j]
        j += 1

print(ans_count)
