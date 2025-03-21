# https://www.acmicpc.net/problem/1916
# hint: visited 대신 weight 를 저장하면서 가면 더 효율적으로 풀 수 있을지도..?


import sys
from heapq import heappush, heappop


def solution():
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        start, end, weight = map(int, input().split())
        graph[start].append((weight, end))

    start, end = map(int, input().split())
    pq = [(0, start)]
    visited = [0] * (n + 1)
    while pq:
        weight, pos = heappop(pq)
        if visited[pos]: continue
        visited[pos] = 1
        if pos == end:
            print(weight)
            break
        for next_weight, next_pos in graph[pos]:
            if not visited[next_pos]:
                heappush(pq, (weight + next_weight, next_pos))


if __name__ == "__main__":
    solution()