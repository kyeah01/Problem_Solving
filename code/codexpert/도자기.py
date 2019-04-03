def solution(k, s):
    global result
    if m == k:
        if arr not in result:
            result += [arr[:]]
        return
    for i in range(s, n):
        arr[k] = soil[i]
        solution(k+1, i+1)

T = int(input())
for tc in range(T):
    n, m = map(int,input().split())
    soil = sorted(list(map(int, input().split())))
    soil.sort()
    arr = [0]*m
    result = []
    solution(0, 0)
    print(len(result))
    # print(result)