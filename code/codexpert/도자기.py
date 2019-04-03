def solution(N,M,soil):
    result = []
    answer = [0]*M
    def comb(k, t):
        nonlocal result
        if t == M:
            # print(answer)
            if answer not in result and answer[::-1] not in result:
                result += [answer[:]]
            return
        for i in range(k, N):
            # answer[k] = soil[i]
            # comb(k+1)
            # comb(k)
            # powerset으로 한다고 가정하면,
            answer[k] = soil[i]
            comb(k+1, t+1)

    comb(0, 0)
    print(result)

T = int(input())

for tc in range(T):
    N, M = map(int,input().split())
    soil = sorted(list(map(int, input().split())))
    solution(N,M,soil)