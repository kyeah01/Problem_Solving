def solution(N,M,soil):
    result = []
    answer = [0]*M
    def comb(k):
        nonlocal result
        if M == k:
            print(answer)
            if answer not in result:
                result += [answer[:]]
            return
        # answer[k] = soil[k]
        for i in range(k+1,N):
            # if k:
            #     if soil[i] < answer[k-1]:
            #         continue
            answer[k] = soil[i]
            comb(k+1)
    comb(0)
    print(result)


T = int(input())

for tc in range(T):
    N, M = map(int,input().split())
    soil = sorted(list(map(int, input().split())))
    solution(N,M,soil)