def solution(n):
    answer = []
    i = 0
    while i < n:
        # print(answer)
        if not answer:
            answer += [boxs[i]]
            i += 1
        else:
            if answer[-1] < boxs[i]:
                answer += [boxs[i]]
                i += 1
            else:
                answer.pop(0)
                i += 1
                
    print(answer)


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    boxs = list(map(int, input().split()))
    print(boxs)
    solution(n)