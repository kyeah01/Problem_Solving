# # 10998. AxB

# a,b = input().split()
# a = int(a)
# b = int(b)

# if 0 < a < 10 and 0 < b < 10:
#     print(a*b)
# else:
#     print("입력가능한 수의 범위를 벗어났습니다.")

# # 1008. A/B

# a,b = input().split()
# a = int(a)
# b = int(b)

# if 0 < a and b < 10:
#     print(a/b)
# else:
#     print("입력가능한 수의 범위를 벗어났습니다.")

# # 10869. 사칙연산

# a,b = input().split()
# a = int(a)
# b = int(b)

# if 1 <= a <= 10000 and 1 <= b <= 10000:
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a//b)
#     print(a%b)
# else:
#     print("입력가능한 수의 범위를 벗어났습니다.")

# # 10430. 나머지

# A,B,C = input().split()
# A = int(A)
# B = int(B)
# C = int(C)

# if 2 <= A <= 10000 and 2 <= B <= 10000 and 2 <= C <= 10000:
#     print((A+B)%C)
#     print((A%C + B%C)%C)
#     print((A*B)%C)
#     print((A%C * B%C)%C)
# else:
#     print("입력가능한 수의 범위를 벗어났습니다.")

# # 2558. A+B ver.2

# a = int(input())
# b = int(input())

# print(a+b)

# # 2839. 설탕배달

# a = int(input())

# if 3 <= a <= 5000:
#     if a == 4 or a == 7:
#         print(-1)
#     elif a % 5 == 0:
#         print(a//5)
#     elif a % 5 == 1:
#         print(a//5+1)
#     elif a % 5 == 2 or a % 5 == 4:
#         print(a//5 + 2)
#     else:
#         print(a//5 + 1)
# else:
#     print("입력가능한 범위의 수가 아닙니다.")