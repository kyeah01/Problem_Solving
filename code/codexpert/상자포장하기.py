def solution(k, a, a_last, b, b_last):
    global maxN
    if n == k:
        maxN = max(maxN, a+b)
        return 
    if a_last > boxs[k]:
        solution(k+1, a+boxs[k], boxs[k], b, b_last)
    if b_last < boxs[k]:
        solution(k+1, a, a_last, b+boxs[k], boxs[k])
    solution(k+1, a, a_last, b, b_last)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    boxs = list(map(int, input().split()))
    # 초기 설정
    maxN = 0
    solution(0,0,1000,0,0)
    print(maxN)