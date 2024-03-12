from collections import deque
import sys


N = int(input())

heap = deque([])
for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        heap.append(x)
        idx = len(heap) - 1
        while idx >= 1:
            if abs(heap[idx]) > abs(heap[idx // 2]):
                break

            elif heap[idx] + heap[idx // 2] == 0 and heap[idx] > 0:
                break

            heap[idx], heap[idx // 2] = heap[idx // 2], heap[idx]
            idx //= 2

    elif heap:
        print(heap.popleft())
        if heap:
            heap.appendleft(heap.pop())
            idx = 0
            while idx < len(heap):
                if 2*idx < len(heap) and (abs(heap[idx]) > abs(heap[2*idx]) or (heap[idx] + heap[2*idx] == 0 and heap[idx] > 0)):
                    if 2*idx + 1 < len(heap) and (abs(heap[2 * idx]) > abs(heap[2 * idx + 1]) or (heap[2 * idx] + heap[2 * idx + 1] == 0 and heap[2 * idx] > 0)):
                        heap[idx], heap[2*idx + 1] = heap[2*idx + 1], heap[idx]
                        idx = 2 * idx + 1
                    else:
                        heap[idx], heap[2 * idx] = heap[2 * idx], heap[idx]
                        idx *= 2
                elif 2*idx + 1 < len(heap) and (abs(heap[idx]) > abs(heap[2 * idx + 1]) or (heap[idx] + heap[2 * idx + 1] == 0 and heap[idx] > 0)):
                    heap[idx], heap[2 * idx + 1] = heap[2 * idx + 1], heap[idx]
                    idx = 2 * idx + 1

                else:
                    break

    else:
        print(0)
