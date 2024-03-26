import sys


N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
# len(cards) <= 500,000 >>>> nlog(n) < 10,000,000
cards.sort()
# log(n) < 20
ans_list = []
for item in nums:
    temp_res = 0
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if cards[mid] == item:
            temp_res = 1
            break

        if cards[mid] < item:
            start = mid + 1

        else:
            end = mid - 1

    ans_list.append(temp_res)

print(*ans_list)