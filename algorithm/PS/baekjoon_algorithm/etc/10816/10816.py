N = int(input())
have = list(map(int, input().split()))
M = int(input())
do_have = list(map(int, input().split()))
have.sort()
for n in do_have:
    start = 0
    end = N - 1
    cnt = 0
    while start <= end:
        mid = (start + end) // 2
        if have[mid] == n:
            temp = mid
            while temp >= 0 and have[temp] == n:
                cnt += 1
                temp -= 1

            cnt -= 1
            temp = mid
            while temp < len(have) and have[temp] == n:
                cnt += 1
                temp += 1

            print(cnt, end=' ')
            break

        elif have[mid] < n:
            start = mid + 1

        else:
            end = mid - 1

    if cnt == 0:
        print(0, end=' ')
