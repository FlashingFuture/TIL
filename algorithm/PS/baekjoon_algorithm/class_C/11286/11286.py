import sys
import heapq


N = int(sys.stdin.readline())
x = [int(sys.stdin.readline()) for _ in range(N)]
m_heap = []         # minus heap
heap = []

for item in x:
    if item == 0:
        if heap and m_heap:
            if m_heap[0] > heap[0]:
                print(heapq.heappop(heap))
            else:
                print(-heapq.heappop(m_heap))

        elif heap:
            print(heapq.heappop(heap))
        elif m_heap:
            print(-heapq.heappop(m_heap))
        else:
            print(0)

    elif item < 0:
        heapq.heappush(m_heap, -item)

    else:
        heapq.heappush(heap, item)
