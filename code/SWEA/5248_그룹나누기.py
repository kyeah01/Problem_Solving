def solution(N, M):
    def mother(x):
        while group[x] != x:
            x = group[x]
        return x
    
    group = list(range(N))
    
    for i in range(0, M*2, 2):
        group[mother(papers[i+1])] = mother(papers[i])
    return sum(1 for i in range(N) if group[i] == i)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    papers = list(map(lambda x:int(x)-1, input().split()))
    print('#{}'.format(tc), solution(N, M))