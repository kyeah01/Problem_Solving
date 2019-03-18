# #  4673. 셀프넘버

# S = list(map(int,range(1,10001)))
# M = []

# for i in S:
#     if i > 9999:
#         M.append(i + (i//1000) + int(str(i)[1]) + int(str(i)[2]) + int(str(i)[3]) + (i%10)) 
#     elif i > 999:
#         M.append(i + (i//1000) + int(str(i)[1]) + int(str(i)[2]) + (i%10)) 
#     elif i > 99 :
#         M.append(i + (i//100) + int(str(i)[1]) + (i%10))        
#     else :
#         M.append(i + (i//10) + (i%10))

# T = sorted(list(set(S)-set(M)))
# for i in range(len(T)):
#     print(T[i])

# # 1065. 한수

# N = int(input())
# L = range(1, N+1)
# M = []

# for i in L:
#     if i < 100:
#         M.append(i)
#     elif 100 < i < 1000:
#         if (i//100) == ((i//10)%10) and ((i//10)%10) == (i%10):
#             M.append(i)
#         elif (i//100) - ((i//10)%10) == ((i//10)%10) - (i%10):
#             M.append(i)

# print(len(M))

# 2448. 별찍기 -11

S = range(10)
M = list(range(10))
n = 0
for k in S:
    M[k] = 3*2**k

N = int(input())
for i in S:         # i는 0부터 9까지
    if N == M[i]:
        if i  == 0:
            M[0][0] = ["  *  "]
            M[0][1] = [" * * "]
            M[0][2] = ["*****"]
            print(M[0])
        else:
            M[0] = ("  *  "'\n'" * * "'\n'"*****") 
            M[i] = "   "*(2**(i-1)) + M[i-1] + "   "*(2**(i-1)) + '\n' + M[i-1] + ' ' + M[i-1]
            print(M[i])