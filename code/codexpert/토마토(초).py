def solution(M,N,H):
    direction = [(-1,0,0), (0,-1,0), (1,0,0), (0,1,0), (0,0,-1), (0,0,1)]
    
    def find_the_first():
        return [(h,n,m,0) for h in range(H) for n in range(N) for m in range(M) if tomatos[h][n][m] == 1]

    def can_i(z,x,y):
        if 0<=z<H and 0<=x<N and 0<=y<M and tomatos[z][x][y] == 0:
            return True
        return False

    def anybody_here():
        for h in range(H):
            for n in range(N):
                for m in range(M):
                    if not tomatos[h][n][m]:
                        return False
        return True
    
    def all_clear():
        for h in range(H):
            for n in range(N):
                for m in range(M):
                    if not tomatos[h][n][m]:
                        return False
        return True

    def ripen():
        time = 0
        if anybody_here():
            print(0)
            return
        queue = find_the_first()
        while queue:
            time += 1
            for _ in range(len(queue)):
                h, i, j, t = queue.pop(0)
                for d in range(6):
                    z = h + direction[d][0]
                    x = i + direction[d][1]
                    y = j + direction[d][2]
                    if can_i(z,x,y):
                        tomatos[z][x][y] = 1
                        queue += [(z,x,y,t+1)]
        print(t) if all_clear() else print(-1)
        return 
    ripen()



# main
M, N, H = map(int,input().split())
tomatos = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
solution(M,N,H)