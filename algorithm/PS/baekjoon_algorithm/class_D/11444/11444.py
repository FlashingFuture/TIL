n = int(input())
# n은 최대 1e18(10^18)
# 2^10 = 10^3이라 하면 대략 2^60 정도의 크기가 최댓값
# 분할정복 시 아마도 60번 정도 재귀가 갈라지면 될 것?
# 당연히 더하면서 갈 순 없고 나머지를 더하면서 이동해야 할 것
# dp로 이동해도 시간초과가 날 것이고 아마도 분할정복으로 나눠서 나머지를 구하는 것
# 아무리 생각해도 알 수 없어서 피보나치 수에 관련된 문제 풀이 글을 확인하여 풀이
# https://www.acmicpc.net/blog/view/28
# 피보나치 수는 F(m+n) = F(m-1)F(n) + F(m)F(n+1)
# 이를 이용하면 F(2n) = (2F(n-1)+F(n))F(n)
# 여기에 홀수를 구하는 경우 F(n+1) = F(n) + F(n-1) 대입 시
# F(2n + 1) = F(n^2) + F((n+1)^2)
# 가 나옴
# 제곱은 분할정복으로 구현 (O(logN))
# 시간초과가 났기에 메모이제이션까지 실행
MOD_NUM = 1000000007
memo = {   # memo_dict 를 피보나치 수열 값으로 초기화
    0: 0,
    1: 1,
    2: 1,
}


def fibonacci(num):
    if num not in memo:
        if num % 2 == 1:
            f_np = fibonacci(num // 2 + 1)
            f_n = fibonacci(num // 2)
            memo[num] = (f_n ** 2 + f_np ** 2) % MOD_NUM
        else:
            f_nm = fibonacci(num // 2 - 1)
            f_n = fibonacci(num // 2)
            memo[num] = (f_n * (f_n + 2*f_nm)) % MOD_NUM

    return memo[num]


print(fibonacci(n))
