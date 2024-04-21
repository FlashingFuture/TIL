from collections import deque


def process(y, x):      # 벽, visited 가 아닌 다음 위치를 처리하는 함수
    if chart[i][j] == '.':  # 이동 가능 공간은 시작 큐에 넣어줌
        queue.append((i, j))
        visited[i][j] = 1
    elif chart[i][j] == '$':
        global stole_docs
        stole_docs += 1
        queue.append((i, j))
        visited[i][j] = 1
    elif chart[i][j].isalpha():  # 알파벳이라면
        if chart[i][j].isupper():  # 문이라면
            if chart[i][j] in keys_list:  # 보유 키에 있다면
                queue.append((i, j))
                visited[i][j] = 1
            else:  # 보유 키에 없다면
                doors_list.append((chart[i][j], i, j))

        else:  # 문이 아닌 알파벳 : 키
            if chart[i][j].upper() not in keys_list:  # 보유 키에 없다면
                keys_list.append(chart[i][j].upper())
                # 이미 방문한 도어 리스트에 해당 키가 있는지 확인
                for door in doors_list:
                    if door[0] == keys_list[-1]:
                        queue.append((door[1], door[2]))
                        visited[i][j] = 1

            queue.append((i, j))
            visited[i][j] = 1


T = int(input())
for tc in range(T):
    h, w = map(int, input().split())    # height / width
    chart = [input() for _ in range(h)]
    keys = input()
    keys_list = [keys[x].upper() for x in range(len(keys))]  # 문은 대문자기에 대문자화
    if keys == '0':
        keys_list = []

    # h, w <= 100
    # 열쇠를 찾는다면, 다시 방문한 길을 돌아가서 들어가야 하는 경우가 생길 수 있음
    # 이 경우, 문을 만났을 때 해당 문의 열쇠와 그 위치를 저장해 놓고
    # 열쇠를 얻을 경우 문을 저장한 배열을 순회하면서 있는지 확인하면 될?듯
    visited = [[0] * w for _ in range(h)]       # 방문 배열
    queue = deque([])                           # BFS 용 큐
    stole_docs = 0                              # 훔친 문서 수를 저장할 배열
    doors_list = []         # 방문했을 때 키가 없었던 위치를 저장할 리스트
    for i in range(h):
        for j in range(w):
            if chart[i][j] == '*':
                visited[i][j] = 1       # 벽은 방문처리

            elif i == 0 or i == h - 1 or j == 0 or j == w - 1:  # 맵의 가장자리에 대해
                process(i, j)

    # 초기 위치를 다 넣었다면 BFS
    while queue:
        start_y, start_x = queue.popleft()
        for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
            i, j = start_y + dy, start_x + dx
            if 0 <= i < h and 0 <= j < w and not visited[i][j]:
                process(i, j)

    print(stole_docs)
