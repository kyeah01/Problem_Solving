def solution(n, target):
    queue = [(n,0)]
    f = 0
    r = 1
    while f != r:
        num, t = queue[f]
        f += 1
        if num == target:
            return t
        
        if num < 1000000:
            nxt = num+1
            queue += [(nxt,t+1)]
            r += 1
        
        if n < target:
            if num <= 500000:
                nxt = num*2
                queue += [(nxt,t+1)]
            r += 1
        
        if num-1 > 0:
            nxt = num-1
            queue += [(nxt,t+1)]
            r += 1
        
        if num > 10:
            nxt = num-10
            queue += [(nxt,t+1)]
            r += 1

        # print(queue)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(solution(N,M))