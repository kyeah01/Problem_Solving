# # 2292. 벌집

# Num = int(input())
# N = 0

# def Seq(N):
#     result = 3*N**2 - 3*N + 1
#     return result

# while True:
#     if Num == 1:
#         print(1)
#         break
#     elif Num <= Seq(N):
#         print(N)
#         break
#     N += 1

# # 1193. 분수찾기

# Num = int(input())
# up = 0
# down = 0
# k =0

# def Seq2(N):
#     result = (N**2 - N +2)//2
#     return result

# while True:
#     if Num < Seq2(k+1):
#         if k % 2 == 0:
#             up = Num - Seq2(k) +1
#             down = k+1-up
#         else:
#             down = Num - Seq2(k) +1
#             up = k+1-down
#         break
#     k += 1

# print(f'{up}/{down}')

# # 1011. Fly me to the Alpha Centauri

# T = int(input())
# count = 0

# for i in range(T):
#     x, y = map(int, input().split())
#     dist = y - x
#     for i in range(1, dist+1):
#         if dist >= i*2:
#             dist -= i*2
#             count += 2
#         else:
#             if 0 < dist <= i:
#                 count += 1
#                 break
#             elif dist > i:
#                 count += 2
#                 break
#     print(count)
#     count = 0

# # 10250. ACM 호텔

# T = int(input())

# for i in range(T):
#     H, W, N = map(int,input().split())
#     if N % H == 0:
#         if (N//H) < 10:
#             print(f'{H}0{N//H}')
#         else:
#             print(f'{H}{N//H}')
#     else:
#         if (N//H+1) < 10:
#             print(f'{N%H}0{(N//H)+1}')
#         else:
#             print(f'{N%H}{(N//H)+1}')

# 2775. 부녀회장이 될테야

# T = int(input())

# N = input()
# B = ['0', '1','2','3','4','5','6','7','8','9']
# C = list(range(10))
# for i in B:
#     C[int(i)] = N.count(i)
# if (C[6]+C[9]) % 2 == 0:
#     C[6] = (C[6] + C[9])//2
# else:
#     C[6] = (C[6] + C[9])//2 + 1
# C[9] = 0
# print(max(C))
