def solution(N, K):
    queue = [(N,0)]
    visited = [N]
    x, e = 0, 1
    while x != e:
        n = queue[x] vgt
        if n[0] == K:
            return n[1]
        if n[0]+1 not in visited:
            queue += [(n[0]+1, n[1]+1)]
            e += 1
        if n[0]-1 not in visited:
            queue += [(n[0]-1, n[1]+1)]
            e += 1
        if n[0]*2 not in visited:
            queue += [(n[0]*2, n[1]+1)]
            e += 1
        x += 1

N, K = map(int, input().split())
print(solution(N,K))