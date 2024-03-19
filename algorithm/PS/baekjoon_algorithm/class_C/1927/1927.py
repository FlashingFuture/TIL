import sys
import heapq


N = int(sys.stdin.readline())
heap = []
x = [int(sys.stdin.readline()) for _ in range(N)]
for item in x:
    if item == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)

    else:
        heapq.heappush(heap, item)
