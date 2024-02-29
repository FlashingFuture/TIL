def kmp_search(txt, pat):
    lps = [0] * (len(pat) + 1)  # longest proper prefix which is suffix
    # lps에는 일치하는 경우들을 저장해 그만큼 kmp 검색 시 이동범위를 조정함
    j = 0  # 일치한 개수(비교할 패턴의 위치)
    lps[0] = -1
    for i in range(1, len(pat)):
        lps[i] = j  # 이전까지 일치한 개수를 lps에 저장
        if pat[i] == pat[j]:
            j += 1      # 일치하는 경우 j값을 올림
        else:
            j = 0       # 일치하지 않는다면 j 초기화

    lps[len(pat)] = j   # 마지막 값에도 j값 저장

    i = 0
    j = 0       # 다시 일치하는 개수를 확인할 j 초기화
    result = 0  # 일치하는 횟수를 저장할 변수
    while i < len(txt) and j <= len(pat):   # 모든 값이 일치해 i가 len(txt)가 되거나,
                                            # lps를 끝까지 순회한 경우
        if j == -1 or txt[i] == pat[j]:     # lps가 -1(첫 글자) or 글자 일치 시
            i += 1
            j += 1
        else:                               # 불일치
            j = lps[j]                          # 불일치한 부분을 건너뜀
        if j == len(pat):                   # j == len(pat). 즉 패턴이 일치하는 경우
            result += 1
            j = lps[j]                      # result를 올리고 불일치한 부분을 건너뜀

    return result


def bf(pattern, text):
    len_t = len(text)
    len_p = len(pattern)
    i = 0   # 전체 텍스트 탐색에 쓸 인덱스
    j = 0   # 패턴 탐색에 쓸 인덱스
    count = 0
    while i < len_t and j < len_p:

        if text[i] != pattern[j]:
            i = i - j + 1
            j = 0

        i += 1
        j += 1

        if j == len_p:
            count += 1
            i = i - j + 1
            j = 0
    return count


for tc in range(1, 11):  # 10번만큼 테스트 반복
    tc_num = int(input())
    P = input()
    text = input()
    ans = kmp_search(text, P)
    print(f'#{tc} {ans}')
