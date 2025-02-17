# https://www.acmicpc.net/problem/4195

import sys


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    fa = find(a)
    fb = find(b)

    if fa != fb:
        parent[fb] = fa
        number[fa] += number[fb]
    print(number[fa])


for _ in range(int(input())):
    num = int(input())
    parent, number = {}, {}
    for i in range(num):
        a, b = sys.stdin.readline().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] =b
            number[b] = 1
        union(a, b)