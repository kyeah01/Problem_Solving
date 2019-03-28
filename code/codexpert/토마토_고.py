def tomato(N, M):
    def ripe(nxt):
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        time = -1
        queue = nxt
        while queue:
            time += 1
            for _ in range(len(queue)):
                x,y = queue.pop(0)
                box[x][y] = 1
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0<= nx < N and 0<= ny <M:
                        if not box[nx][ny] and (nx, ny) not in queue:
                            queue += [(nx, ny)]
        for i in range(N):
            if 0 in box[i]:
                return -1
        return time

    maxN = 0
    nxt = [(i,j) for i in range(N) for j in range(M) if box[i][j] == 1]
    if len(nxt) == M*N:
        return 0
    return ripe(nxt)

# main
M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
print(tomato(N,M))