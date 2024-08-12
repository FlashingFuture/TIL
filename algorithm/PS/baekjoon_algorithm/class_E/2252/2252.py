import sys
from collections import deque


def top_sort(n, graph, in_degree):
    queue = deque(i for i in range(1, n + 1) if in_degree[i] == 0)
    result = []

    while queue:
        curr = queue.popleft()
        result.append(curr)

        for neighbor in graph[curr]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result


def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        in_degree[b] += 1

    result = top_sort(n, graph, in_degree)
    print(*result)


if __name__ == "__main__":
    main()
