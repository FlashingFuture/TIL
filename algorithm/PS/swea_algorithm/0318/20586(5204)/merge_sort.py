# def merge_sort(s):
#     if len(s) == 1:
#         return s
#
#     s1, s2 = [], []
#     for i in range(len(s) // 2):
#         s1.append(s[i])
#
#     for i in range(len(s) // 2, len(s)):
#         s2.append(s[i])
#
#     s1 = merge_sort(s1)
#     s2 = merge_sort(s2)
#     return merge(s1, s2)
#
#
# def merge(l, r):
#     m = []
#     l_cnt, r_cnt = 0, 0
#     while l_cnt < len(l) or r_cnt < len(r):
#         if l_cnt < len(l) and r_cnt < len(r):
#             if l[l_cnt] <= r[r_cnt]:
#                 m.append(l[l_cnt])
#                 l_cnt += 1
#             else:
#                 m.append(r[r_cnt])
#                 r_cnt += 1
#
#         elif l_cnt < len(l):
#             global cnt
#             cnt += 1
#             m.extend(l[l_cnt:])
#             break
#         elif r_cnt < len(r):
#             m.extend(r[r_cnt:])
#             break
#
#     return m
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     a = list(map(int, input().split()))
#     cnt = 0
#     res_deq = merge_sort(a)
#     print(f'#{tc} {res_deq[N // 2]} {cnt}')


def merge_sort(a):
    # a : 분할해야하는 리스트
    global answer
    if len(a) == 1:
        return a

    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    l = 0
    r = 0
    i = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            a[i] = left[l]
            l += 1
        else:
            a[i] = right[r]
            r += 1
        i += 1


T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end = ' ')
    N = int(input())
    A = list(map(int, input().split()))
    answer = 0
    print(A[N // 2], answer)