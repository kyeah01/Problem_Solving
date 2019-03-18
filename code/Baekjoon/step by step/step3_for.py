# # 2741. N찍기

# N = int(input())

# for i in range(1, N+1):
#     print(i)

# # 2742. 기찍N

# N = int(input())

# for i in range(N):
#     print(N-i)

# # 2739. 구구단

# N = int(input())

# if 1 <= N <= 9:
#     for i in range(1,10):
#         print( N,"*", i,"=" , N*i)
# else:
#     print("입력가능한 범위의 숫자가 아닙니다.")

# # 2438. 별찍기

# N = int(input())

# for i in range(1,N+1):
#     print(i*'*')

# # 2439. 별찍기 -2

# N = int(input())

# for i in range(N):
#     print((N-i-1)*' ',end ='')
#     print((i+1)*'*')

# # 2440. 별찍기 -3

# N = int(input())

# for i in range(N):
#     print((N-i)*'*')

# # 2441. 별찍기

# N = int(input())

# for i in range(N):
#     print((i)*' ',end='')
#     print((N-i)*'*')

# # 1924. 2007년

# month,day = input().split()
# day = int(day)
# month = int(month) -1
# week = {0:'SUN', 1:'MON', 2:'TUE', 3:'WED', 4:'THU', 5:'FRI', 6:'SAT'}

# for i in range(month):
#     if month == 0:
#         break
#     else:
#         if month == 2:
#             day += 28
#             month -= 1
#         elif month in [ 4, 6, 9, 11]:
#             day += 30
#             month -= 1
#         else:
#             day += 31
#             month -= 1

# print(week[(day%7)])

# # 8393. 합

# N = int(input())
# total = 0

# for i in range(1,N+1):
#     total+=i
# print(total)

# # 11720. 숫자의 합

# N = int(input())
# A = list(input())
# T = 0


# for i in range(N):
#     A[i] = int(A[i])
#     T += A[i]

# print(T)

# # 11721. 열개씩 끊어 출력하기

# S = input()
# L = len(S)
# N = list(range(L//10))
# T=[]

# for i in N:
#     T += [i*10]

# for i in T:
#     P = S[i:(i+10)]
#     print(P)

# if L%10 != 0:
#     print(S[-(L%10):])

# 15552. 빠른 A+B

import sys

T = int(sys.stdin.readline())
A = 0

for i in range(T):
    B = sys.stdin.readline().split()
    for i in range(2):
        B[i] = int(B[i])
        A += B[i]
    print(A)
    A = 0