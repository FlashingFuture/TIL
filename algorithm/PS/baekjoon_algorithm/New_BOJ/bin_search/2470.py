# https://www.acmicpc.net/problem/2470
# N <= 100,000 이므로 리스트 정렬 후
# 두 포인터를 움직이면서 계속 최저값을 찾으면?

def main():
    N = int(input())
    values = list(map(int, input().split()))
    values.sort()

    start = 0
    end = N - 1
    min_value = 2000000000
    min_left = -1000000000
    min_right = 1000000000

    while start <= end:
        curr_value = values[start] + values[end]
        if abs(curr_value) < min_value:
            min_value = abs(curr_value)
            min_left, min_right = values[start], values[end]
        # 현재 혼합값이 양수면 산성값을 왼쪽으로, 아니면 알칼리값을 오른쪽으로 이동
        if min_value == 0:
            break
        if curr_value > 0:
            end -= 1
        else:
            start += 1

    print(min_left, min_right)

if __name__ == "__main__":
    main()