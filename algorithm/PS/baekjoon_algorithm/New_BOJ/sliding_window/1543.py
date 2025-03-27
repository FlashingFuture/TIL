# https://www.acmicpc.net/problem/15961

import sys
input = sys.stdin.readline


def init():
    n, d, k, c = map(int, input().split())
    belt = [int(input()) for _ in range(n)]

    count = [0] * (d + 1)
    unique = 0

    for i in range(k):
        if count[belt[i]] == 0:
            unique += 1
        count[belt[i]] += 1

    max_unique = unique + (1 if count[c] == 0 else 0)

    for i in range(1, n):
        remove_sushi = belt[i - 1]
        count[remove_sushi] -= 1
        if count[remove_sushi] == 0:
            unique -= 1

        add_sushi = belt[(i + k - 1) % n]
        if count[add_sushi] == 0:
            unique += 1
        count[add_sushi] += 1

        total = unique + (1 if count[c] == 0 else 0)
        max_unique = max(max_unique, total)

    print(max_unique)


if __name__ == "__main__":
    init()