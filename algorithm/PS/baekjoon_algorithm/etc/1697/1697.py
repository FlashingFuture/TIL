from collections import deque


N, K = map(int, input().split())
queue = deque([N])
visited = [0] * 100001
while queue:
    pos = queue.popleft()
    if pos == K:
        print(visited[pos])
        break
    if not visited[pos - 1] and pos >= 1:
        queue.append(pos - 1)
        visited[pos - 1] = visited[pos] + 1

    if  pos < 100000 and not visited[pos + 1]:
        queue.append(pos + 1)
        visited[pos + 1] = visited[pos] + 1

    if pos <= 50000 and not visited[2*pos]:
        queue.append(2*pos)
        visited[2*pos] = visited[pos] + 1
