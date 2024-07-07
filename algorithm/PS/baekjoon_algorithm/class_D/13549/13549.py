from collections import deque


def solution():
    N, K = map(int, input().split())

    # 길이 100001짜리 배열을 선언하고 bfs 로 풀이
    arr = [-1] * 100001
    queue = deque([(N, 0)])
    arr[N] = 0
    while queue:
        pos, time = queue.popleft()
        # 우선 0 시간이 소모되는 2배 이동을 우선적으로 처리
        if pos <= 50000 and arr[2*pos] == -1:
            arr[2*pos] = time
            queue.appendleft((2*pos, time))

        # 그 후 1 시간이 소모되는 이동은 평범하게 bfs 처럼 처리
        if pos > 0 and arr[pos - 1] == -1:
            arr[pos - 1] = time + 1
            queue.append((pos - 1, time + 1))
        if pos < 100000 and arr[pos + 1] == -1:
            arr[pos + 1] = time + 1
            queue.append((pos + 1, time + 1))

    print(arr[K])


if __name__ == '__main__':
    solution()
