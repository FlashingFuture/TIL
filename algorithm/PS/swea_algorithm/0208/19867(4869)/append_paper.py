T = int(input())
for tc in range(T):     # T번만큼 테스트 반복
    N = int(input())
    paper_case = [1, 3]     # 1일 때 1, 2일 때 3
    for i in range(2, N // 10):
        paper_case.append(paper_case[i - 1] + 2 * paper_case[i - 2])

    print(f'#{tc + 1} {paper_case.pop()}')


