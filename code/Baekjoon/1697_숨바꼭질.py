def solution(N, K):
    queue = [(N,0)]
    visited = [N]
    x, e = 0, 1
    while x != e:
        print(queue)
        n = queue[x]
        if n[0] == K:
            return n[1]
        if n[0]+1 not in visited and n[0]+1 <= K:
            if n[0]+1 == K:
                return n[1]+1
            queue += [(n[0]+1, n[1]+1)]
            visited += [n[0]+1]
            e += 1
        if n[0]-1 not in visited and n[0]-1 >= 0:
            if n[0]-1 == K:
                return n[1]+1
            queue += [(n[0]-1, n[1]+1)]
            visited += [n[0]-1]
            e += 1
        if n[0]*2 not in visited and n[0]*2 <= K+1:
            if n[0]*2 == K:
                return n[1]+1
            queue += [(n[0]*2, n[1]+1)]
            visited += [n[0]*2]
            e += 1
        x += 1

N, K = map(int, input().split())
print(solution(N,K))