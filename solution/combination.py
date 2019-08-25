# # powerset 구하기

# # 1. 재귀이용.
# def powerset(k, n, arr):
#     if k == n:
#         for i in range(n):
#             if arr[i]:
#                 print(target[i], end='')
#         print()
#         return
#     else:
#         arr[k] = 0
#         powerset(k+1, n, arr)
#         arr[k] = 1
#         powerset(k+1, n, arr)

# target = [1,2,3,4]
# arr = [1]*len(target)
# powerset(0, len(target), arr)


def powerset(s):
    x = len(s)
    for i in range(1 << x):
        print([s[j] for j in range(x) if (i & (1 << j))])

target = [1,2,3,4]
powerset(target)