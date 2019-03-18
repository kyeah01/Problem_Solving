# # 1152. 단어의 개수

# A = input().split()
# print(len(A))

# # 2577. 숫자의 개수

# A = int(input())
# B = int(input())
# C = int(input())
# T = list(map(int,str(A*B*C)))
# ct = 0

# for x in range(10):
#     for i in T:
#         if x == i:
#             ct += 1
#     print(ct)
#     ct = 0

# # 8958.OX 퀴즈

# N = int(input())
# a = 0
# T = 0
# M = []

# while N:
#     A = input().split()
#     M.append(A)
#     N -= 1
#     if N == 0 : break

# for i in range(1, N+1):
#     for j in len(M[i]):
#         if M[i][j] == 'O':
#             a += 1
# print(a) 

# # 2920. 음계

# import sys

# A = sys.stdin.readline().split()
# A = list(map(int,A))
# keys = list(range(1,9))

# if A == keys:
#     print("ascending")
# elif A == keys[::-1]:
#     print("descending")
# else:
#     print("mixed")

# # 10039. 평균점수

# def dict(**args):
#     for i in args:
#         args[i] = args[i]
#         return args

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())

# scores = dict(원섭=a, 세희=b, 상근=c, 숭=d, 강수=e)

# total = 0
# for i in scores.keys():
#     if scores[i] < 40:
#         scores[i] = 40
#     total += scores[i]
# print(int(total/len(scores)))