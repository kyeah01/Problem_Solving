# # 9498. 시험성적

# score = int(input())

# A = { 10:"A", 9:"A", 8:"B", 7:"C", 6:"D" }

# if  score//10 in A.keys() :
#     print(A[(score//10)])
# else:
#     print("F")

# # 10817. 세 수

# L = list(map(int,input().split()))

# L.sort()

# print(L[1])

# # 10871. X보다 작은 수

# import sys

# N, X = map(int,sys.stdin.readline().split())
# A = list(map(int,sys.stdin.readline().split()))

# for i in range(N):
#     if A[i] < X:
#         print(A[i])

# # 1546. 평균

# import sys

# N = int(sys.stdin.readline())
# M = list(map(int, sys.stdin.readline().split()))
# T = 0

# M.sort()
# B = M[N-1]

# for i in range(N):
#     M[i] = M[i] / B*100
#     T += M[i]
# print(T/N)

# # 4344. 평균은 넘겠지

# import sys

# C = int(sys.stdin.readline())
# F = list(range(C))
# T = 0
# ct = 0

# for i in F:
#     ct = 0
#     T = 0
#     F[i] = list(map(int,sys.stdin.readline().split()))
#     for j in range(1, F[i][0]+1):
#         T += F[i][j]
#     Avg = T/F[i][0]
#     for j in range(1, F[i][0]+1):
#         if F[i][j] > Avg:
#             ct += 1
#     F[i] = format(ct/F[i][0]*100, '.3f')

# for i in range(C):
#     print(F[i], end ='% \n')

# # 1110. 더하기 사이클

# C = input()
# N = C
# A = 0
# ct = 0 

# while True:
#     if int(N) < 10:
#         N = str(int(N)) + str(int(N))
#         ct += 1
#     else:
#         ct += 1
#         A = int(N[0]) + int(N[1])
#         if len(str(A)) == 2:
#             N = str(N[1]) + str(A)[1]
#         else:
#             N = str(N[1]) + str(A)
#     if int(C) == int(N): break
# print(ct)