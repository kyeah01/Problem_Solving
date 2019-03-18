# print(ord(input()))

# # 10809. 알파벳찾기

# from string import ascii_lowercase
# S = input()
# value = 0
# B =[]
# A = list(ascii_lowercase)

# for i in range(len(A)):
#     for j in range(len(S)):
#         if S[j]==A[i]:
#             value = j
#             break
#     else:
#         value = -1
#     B.append(value)
# print(*B)

# # 2675. 문자열 반복

# T = int(input())
# C = T
# A = [0, 0]

# while C:
#     A[0], A[1] = input().split()
#     C -= 1
#     for j in range(len(A[1])):
#         print(A[1][j]*int(A[0]), end ='')
#     print()
#     if C == 0 : break

# 1157. 단어 공부
# from string import ascii_uppercase

# B = [0 for i in range(26)]
# Alpha = input().upper()
# return_Alpha = 0
# a = 0

# for i in range(26):
#     for j in range(len(Alpha)):
#         if Alpha[j] == ascii_uppercase[i]:
#             B[i] += 1

# if B.count(max(B)) == 1:
#     for i in range(len(B)):
#         if max(B) == B[i]:
#             print(ascii_uppercase[i])
# else:
#     print("?")

# # 1316. 그룹단어체커

# N = int(input())
# A =[]
# Prove = []
# snumber = 0

# for i in range(N):
#     a = input()
#     A.append(a)
#     for k in range(len(A[i])):
#         if A[i][k] not in Prove:
#             Prove.append(A[i][k])
#         elif A[i][k] != A[i][k-1]:
#             break
#     else:
#         snumber += 1
#     Prove = []
# print(snumber)

# # 2908. 상수

# def sangsu(sentenceA, sentenceB):
#     setenceA = int(sentenceA)
#     setenceB = int(sentenceB)
#     if sentenceA >= sentenceB:
#         return sentenceA
#     else:
#         return sentenceB

# numberA , numberB = input().split()
# numberA = numberA[::-1]
# numberB = numberB[::-1]
# print(sangsu(numberA, numberB))

# # 5622. 다이얼

# dial = {3:['A','B','C'], 4:['D','E','F'], 5:['G','H','I'], 6:['J','K','L'], 7:['M','N','O'], 8:['P','Q','R','S'], 9:['T','U','V'], 10:['W','X','Y','Z']}
# num = input()
# return_number = 0

# for i in range(len(num)):
#     for j in range(3,11):
#         if num[i] in dial[j]:
#             return_number += j

# print(return_number)

# 2941. 크로아티아 알파벳
iValue = input()
rValue = 0
for i in range(len(iValue)):
    if iValue[i] == '=':
        rValue -= 1
        if iValue[i-1] == 'z' and iValue[i-2] == 'd':
            rValue -= 1
    elif iValue[i] == '-':
        rValue -= 1
    elif iValue[i] == 'j':
        if iValue[i-1] == 'l' or iValue[i-1] == 'n':
            rValue -= 1
    rValue +=1
print(rValue)