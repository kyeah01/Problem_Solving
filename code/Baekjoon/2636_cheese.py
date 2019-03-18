def AIR():
    dxy = [0,0,-1,1]
    for d in range(4):
        if not board[i+dxy[d]][j+dxy[::-1][d]]:
            k, t = i+dxy[d]*2, j+dxy[::-1][d]*2
            while 0<=k<S and 0<=t<G:
                if board[k][t]:
                    break
                k += i+dxy[d]
                t += dxy[::-1][d]
            else:
                board[i+dxy[d]][j+dxy[::-1][d]] = 'c'
    
            

S, G = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(S)]
for s in range(S):
    for g in range(G):
        if board[s][g] == 1:
            AIR()