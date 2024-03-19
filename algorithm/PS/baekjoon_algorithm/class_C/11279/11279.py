import sys
import heapq


N = int(sys.stdin.readline())
x = [int(sys.stdin.readline()) for _ in range(N)]
heap = []
for item in x:
    if not item:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)

    else:
        heapq.heappush(heap, -item)
