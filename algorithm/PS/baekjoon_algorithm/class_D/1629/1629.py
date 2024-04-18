import sys


# 알고리즘 분류 : 분할 정복을 이용한 거듭제곱
# B가 2^32 - 1이라고 했을 때, 분할정복을 이용하면 대락 32번 2개씩 분할하여
# 나머지가 아닌 몫인 부분에 곱하는 것은 무시해도 됨을 이용
# 결과에 도달할 수 있을 것


def get_num(b):
    if b == 1:
        return A % C

    elif b % 2 == 1:
        return (get_num(b // 2)**2) * A % C
    return (get_num(b // 2)**2) % C


A, B, C = map(int, sys.stdin.readline().split())
print(get_num(B))
