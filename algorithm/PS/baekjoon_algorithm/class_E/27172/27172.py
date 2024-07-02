import sys


N = int(input())
x = list(map(int, sys.stdin.readline().split()))
# N은 최대 10만
# 완전 탐색 시 O(N^2)으로 시간초과가 날 것
# 따라서 전체 수 범위(100만)을 탐색하면서 해시에 넣는 방식으로 풀이
# 우선 x의 모든 원소를 딕셔너리의 key로 설정
answer_dict = dict()
for item in x:
    answer_dict[item] = 0

x.sort()    # x를 정렬하여 나누는 연산을 정상적으로 실행할 수 있도록 함
max_num = x[-1]

for item in x:
    # item 의 배수만큼 곱해가면서 승패를 결정
    for num in range(item * 2, max_num + 1, item):
        if num in answer_dict:
            answer_dict[item] += 1
            answer_dict[num] -= 1


for key, value in answer_dict.items():
    print(value, end=" ")
