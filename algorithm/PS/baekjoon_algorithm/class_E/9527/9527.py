# A, B 의 크기는 최대 10^16
# 둘의 값 차이를 DP로 계산하기에는 너무 큰 차이
# 둘을 이진수화 한 다음 차수를 하나씩 올려가면서 비교하면 될?듯
# 가장 큰 차수부터 비교하면서 어떻게 2를 곱하면 되지 않을까?
# 반대로 생각하면 아래 자리는 차수가 올라갈수록 반복 패턴이 발생하므로
# 한 차수씩 내리면서 분할정복 / 누적합 느낌으로 풀면 될듯


def total_sum(n):
    count = 0

    degree = 0  # 이진수의 차수
    while 2 ** degree <= n:
        max_digit = 2 ** (degree + 1)   # 다음 차수의 값 ( 1000...)
        # 해당 차수의 최대 차수가 아닌 모든 수는 0과 1이 반씩 균등하게 나옴
        count += ((n + 1) // max_digit) * (max_digit // 2)
        # 혹시 남은 부분이 있다면(최대 차수에 도달했다면)
        # 최대 차수의 값만큼 count 에 더해줌
        count += max(0, (n + 1) % max_digit - max_digit // 2)

        degree += 1

    return count


A, B = map(int, input().split())
res = total_sum(B) - total_sum(A - 1)
print(res)