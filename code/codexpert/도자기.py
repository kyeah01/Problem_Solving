# def solution(k, s):
#     global result
#     if m == k:
#         if arr not in result:
#             result += [arr[:]]
#         return
#     for i in range(s, n):
#         arr[k] = soil[i]
#         solution(k+1, i+1)

def solution(k, s):
    global sol
    if m == k:
        sol += 1
        return
    for i in range(s, n):
        if arr[k] != soil[i]:
            arr[k] = soil[i]
            solution(k+1, i+1)
    arr[k] = 0


T = int(input())
for tc in range(T):
    n, m = map(int,input().split())
    soil = sorted(list(map(int, input().split())))
    soil.sort()
    arr = [0]*m
    sol= 0
    solution(0, 0)
    print(sol)
    # print(result)