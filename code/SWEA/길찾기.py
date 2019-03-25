import sys, time
sys.stdin = open('input.txt')

# # 완전검색 하는 경우

# T = int(input())

# def permutation(a):
#     arr = []
#     n = len(a)
#     def perm(n, k):
#         nonlocal arr
#         if n == k:
#             value = 0
#             now = home
#             for nxt in a:
#                 value += abs(nxt[0]-now[0]) + abs(nxt[1]-now[1])
#                 now = nxt
#             value += abs(office[0]-now[0]) + abs(office[1]-now[1])
#             arr += [value]
#         else:
#             for i in range(k, n):
#                 a[i], a[k] = a[k], a[i]
#                 perm(n, k+1)
#                 a[i], a[k] = a[k], a[i]
#     perm(n,0)
#     return min(arr)

# for tc in range(1, T+1):
#     n = int(input())
#     maps = [[0 for _ in range(100)] for _ in range(100)]
#     points = list(map(int, input().split()))
#     home, office = points[0:2], points[2:4]
#     points = [[points[i], points[i+1]] for i in range(4, (n+2)*2, 2)]
#     arr = []
#     print(permutation(points))

# 가지치기 하는 경우

T = int(input())

start_time = time.time()

def permutation(a):
    arr = []
    n = len(a)
    minN = 1000000
    def perm(n, k, value, now):
        nonlocal arr, minN
        if n == k:
            value += abs(office[0]-now[0]) + abs(office[1]-now[1])
            arr += [value]
            minN = min(value, minN)
        else:
            for i in range(k, n):
                a[i], a[k] = a[k], a[i]
                nxt = value + abs(a[k][0]-now[0])+ abs(a[k][1]-now[1])
                if nxt > minN:
                    a[i], a[k] = a[k], a[i]
                    continue
                perm(n, k+1, nxt, a[k])
                a[i], a[k] = a[k], a[i]
    perm(n, 0, 0, home)
    return min(arr)

for tc in range(1, T+1):
    n = int(input())
    maps = [[0 for _ in range(100)] for _ in range(100)]
    points = list(map(int, input().split()))
    home, office = points[0:2], points[2:4]
    points = [[points[i], points[i+1]] for i in range(4, (n+2)*2, 2)]
    print(permutation(points))

print(time.time()-start_time)
