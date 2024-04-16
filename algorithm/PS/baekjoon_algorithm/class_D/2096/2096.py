import sys
# Python에서 int의 크기는 운영체제 64bit 기준으로 8byte = 8000bit
# 4MB 제한에 대해 쓸 수 있는 크기는 500,000(4bit일 경우 1,000,000)
# 시간복잡도는 dp시 100000x3x2=600000이기에 시간이 넘치므로
# 1줄짜리 배열 두개 만들어서 하나씩 넘기고 갱신하면서 진행해도
# 시간복잡도는 1200000으로 매우 여유있음
# arr 인풋을 한꺼번에 받기만 해도 메모리초과가 발생해버림
# 인풋도 한줄씩 받으면서 dp를 갱신
N = int(input())
arr = list(map(int, input().split()))
last_SDP = [arr[x] for x in range(3)]    # smallest DP
last_BDP = [arr[x] for x in range(3)]    # biggest DP
new_SDP = [0] * 3
new_BDP = [0] * 3


for i in range(1, N):
    arr = list(map(int, sys.stdin.readline().split()))

    new_SDP[0] = arr[0] + min(last_SDP[0], last_SDP[1])
    new_SDP[1] = arr[1] + min(last_SDP)
    new_SDP[2] = arr[2] + min(last_SDP[1], last_SDP[2])

    last_SDP = [new_SDP[x] for x in range(3)]

    new_BDP[0] = arr[0] + max(last_BDP[0], last_BDP[1])
    new_BDP[1] = arr[1] + max(last_BDP)
    new_BDP[2] = arr[2] + max(last_BDP[1], last_BDP[2])

    last_BDP = [new_BDP[x] for x in range(3)]

if N == 1:
    new_BDP, new_SDP = last_BDP, last_SDP
print(max(new_BDP), min(new_SDP))
